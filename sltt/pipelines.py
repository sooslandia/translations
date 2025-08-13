import logging
import shutil
import urllib.parse
from pathlib import Path

import git

from sltt import context, schema
from sltt.enums import PipelineType
from sltt.repo_registry import repo_registry
from sltt.settings import config
from sltt.stages.base import BaseStage
from sltt.stages.registry import stage_registry

logger = logging.getLogger(__name__)

operation_modes = {
    "pull": (
        PipelineType.PULL
        | PipelineType.SOURCE_CONVERSIONS
        | PipelineType.TRANSLATION_CONVERSIONS
    ),
    "new_commits": (
        PipelineType.SOURCE_CONVERSIONS | PipelineType.TRANSLATION_CONVERSIONS
    ),
    "pull_request": (PipelineType.TRANSLATION_CONVERSIONS | PipelineType.PREVIEW),
    "push": PipelineType.PUSH,
}

GIT_ENV = {
    "GIT_LFS_SKIP_SMUDGE": "1",
    "GIT_TERMINAL_PROMPT": "0",
    "GIT_ASKPASS": config.git_askpass,
    "GITHUB_TOKEN": config.github_token.get_secret_value(),
}


def run_stages(
    *,
    pipeline_name: str,
    stages: list[schema.Stage],
    source_root: Path,
    target_root: Path,
    repository_dir: Path | None,
):
    logger.info(f"Running {len(stages)} stages in pipeline {pipeline_name}")
    current_context = {"pipeline_name": pipeline_name, "total_stages": len(stages)}
    for i, stage_config in enumerate(stages, start=1):
        stage_impl = stage_registry.get(stage_config)
        if stage_impl is None:
            raise NotImplementedError(
                f"No implementation found for stage {stage_config.type}"
            )
        current_context["stage_number"] = i
        current_context["stage_name"] = stage_config.type
        try:
            token = context.current_stage_context.set(current_context.copy())
            logger.info(f"Running stage {i}: {stage_config.type}")
            _run_stage(
                source_root, target_root, repository_dir, stage_config, stage_impl
            )
        finally:
            context.current_stage_context.reset(token)
    logger.info("All stages ran")


def _run_stage(
    source_root: Path,
    target_root: Path,
    repository_dir: Path | None,
    stage_config: schema.Stage,
    stage_impl: BaseStage,
):
    stage = stage_impl(
        source_root=source_root, target_root=target_root, config=stage_config
    )
    stage.run()
    if repository_dir is not None:
        stage.stage_changes(repo=repo_registry.get_repo(repository_dir))


def _clone_repo(repo_url: str) -> Path:
    if ":" not in repo_url:
        repo_url = "https://github.com/" + repo_url
    repo_path = urllib.parse.urlsplit(repo_url).path.lstrip("/")
    source_repo_dir = config.source_repositories_dir / repo_path
    if source_repo_dir.exists():
        raise RuntimeError(
            f"Failed to clone repository, directory {source_repo_dir} already exists"
        )
    source_repo_dir.mkdir(parents=True)
    logger.info(
        f"Cloning repository {repo_url} to "
        f"{source_repo_dir.relative_to(config.repository_dir)}"
    )
    git.Repo.clone_from(repo_url, source_repo_dir, env=GIT_ENV)
    logger.info("Repository cloned")
    return source_repo_dir


def run_pull_pipeline(*, project_root: Path, pull_configs: list[schema.PullConfig]):
    logger.info(f"Running pull pipeline, config count: {len(pull_configs)}")
    pull_configs_with_repos: list[tuple[Path, schema.PullConfig]] = []
    # Clone all repos first instead of cloning and running stages for every repo,
    # to failfast if cloning failed.
    for pull_config in pull_configs:
        repo_dir = _clone_repo(pull_config.repository)
        pull_configs_with_repos.append((repo_dir, pull_config))
    for repo_dir, pull_config in pull_configs_with_repos:
        run_stages(
            pipeline_name="pull",
            stages=pull_config.stages,
            source_root=repo_dir,
            target_root=project_root,
            repository_dir=config.projects_dir,
        )
        logger.debug(f"Removing repository: {repo_dir}")
        shutil.rmtree(repo_dir)
        logger.debug("Repository removed")


def run_source_conversions_pipeline(*, project_root: Path, stages: list[schema.Stage]):
    logger.info(f"Running source conversions pipeline, stage count: {len(stages)}")
    run_stages(
        pipeline_name="source_conversions",
        stages=stages,
        source_root=project_root,
        target_root=project_root,
        repository_dir=config.projects_dir,
    )


def run_translation_conversions_pipeline(
    *, project_root: Path, stages: list[schema.Stage]
):
    logger.info(f"Running translation conversions pipeline, stage count: {len(stages)}")
    run_stages(
        pipeline_name="translation_conversions",
        stages=stages,
        source_root=project_root,
        target_root=project_root,
        repository_dir=config.projects_dir,
    )


def run_push_pipeline(*, project_root: Path, push_configs: list[schema.PushConfig]):
    logger.info(f"Running push pipeline, config count: {len(push_configs)}")
    push_configs_with_repos: list[tuple[Path, schema.PushConfig]] = []
    for push_config in push_configs:
        repo_dir = _clone_repo(push_config.repository)
        push_configs_with_repos.append((repo_dir, push_config))
    repos_to_push: list[Path] = []
    for repo_dir, push_config in push_configs_with_repos:
        run_stages(
            pipeline_name="push",
            stages=push_config.stages,
            source_root=project_root,
            target_root=repo_dir,
            repository_dir=repo_dir,
        )
        # Commit everything here and push in other loop
        # to minimize chance of inconsistency due to error.
        commit_created = _commit_changes(repo_dir)
        if commit_created:
            repos_to_push.append(repo_dir)
    logger.debug(f"Pushing {len(repos_to_push)} repos")
    for repo_dir in repos_to_push:
        _push_repo(repo_dir)
    for repo_dir, _ in push_configs_with_repos:
        logger.debug(f"Removing repository: {repo_dir}")
        shutil.rmtree(repo_dir)
        logger.debug("Repository removed")


def _commit_changes(repo_dir: Path) -> bool:
    logger.debug(f"Creating commit in repo {repo_dir}")
    repo = repo_registry.get_repo(repo_dir)
    index = repo.index
    staging_is_empty = not bool(index.diff("HEAD"))
    if staging_is_empty:
        logger.debug("Nothing to commit")
        return False
    author = git.Actor("SLTT", config.email_address)
    commit = index.commit("Update translations", author=author, committer=author)
    logger.debug(f"Commit created: {commit.hexsha}")
    return True


def _push_repo(repo_dir: Path):
    logger.info(f"Pushing repository: {repo_dir}")
    repo = repo_registry.get_repo(repo_dir)
    repo.remote().push(env=GIT_ENV)
    logger.info("Repository pushed")


def run_preview_pipeline(*, project_root: Path, stages: list[schema.Stage]):
    stage_count = len(stages)
    logger.info(f"Running preview pipeline, stage count: {stage_count}")
    if stage_count == 0:
        logger.info("No stages, doing nothing")
        return
    preview_dir = config.preview_dir / project_root.name
    preview_dir.mkdir(parents=True, exist_ok=True)
    run_stages(
        pipeline_name="preview",
        stages=stages,
        source_root=project_root,
        target_root=preview_dir,
        repository_dir=None,
    )
