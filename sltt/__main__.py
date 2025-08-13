import logging
import sys
from argparse import ArgumentParser
from pathlib import Path

import yaml

from sltt import pipelines, schema
from sltt.enums import PipelineType
from sltt.logging_utils import setup_logging
from sltt.message_manager import message_manager
from sltt.settings import config

logger = logging.getLogger("sltt.__main__")


def create_arg_parser():
    parser = ArgumentParser("sltt", description="Sooslandia translation tool")
    parser.add_argument(
        "--mode", choices=pipelines.operation_modes.keys(), required=True
    )
    return parser


def load_projects(config_file: Path) -> list[schema.Project]:
    raw_config = config_file.read_bytes().decode()
    config_data = yaml.safe_load(raw_config)
    projects = []
    for name, project_data in config_data.items():
        try:
            project = schema.Project(name=name, **project_data)
        except Exception:
            print(f"Error when loading project {name}")
            raise
        projects.append(project)
    return projects


def handle_project(project: schema.Project, pipeline_flags: int):
    logger.info(f'Running pipelines for project "{project.name}"')
    project_root = config.projects_dir / project.name
    if not project_root.exists():
        logger.info("Project directory not found, creating project directory")
        project_root.mkdir()
    for member in PipelineType:
        if not member & pipeline_flags:
            continue
        logger.info(f"Running {member.name} pipeline")
        match member:
            case PipelineType.PULL:
                pipelines.run_pull_pipeline(
                    project_root=project_root, pull_configs=project.pull_configs
                )
            case PipelineType.SOURCE_CONVERSIONS:
                pipelines.run_source_conversions_pipeline(
                    project_root=project_root, stages=project.source_conversions
                )
            case PipelineType.TRANSLATION_CONVERSIONS:
                pipelines.run_translation_conversions_pipeline(
                    project_root=project_root, stages=project.translation_conversions
                )
            case PipelineType.PUSH:
                pipelines.run_push_pipeline(
                    project_root=project_root, push_configs=project.push_configs
                )
            case PipelineType.PREVIEW:
                pipelines.run_preview_pipeline(
                    project_root=project_root, stages=project.preview_config
                )
        logger.info(f"{member.name} pipeline finished")


def main():
    setup_logging()
    parser = create_arg_parser()
    cmd_args = parser.parse_args()
    mode_pipeline_flags = pipelines.operation_modes[cmd_args.mode]
    pipeline_names = [
        member.name for member in PipelineType if member & mode_pipeline_flags
    ]
    logger.info(
        f"Working in mode {cmd_args.mode}, pipelines to run: {', '.join(pipeline_names)}"
    )
    logger.debug(f"Config: {config.model_dump_json(indent=2)}")
    projects = load_projects(config.projects_file)
    logger.info(f"Loaded {len(projects)} projects")
    error_messages = []
    for project in projects:
        handle_project(project, mode_pipeline_flags)
        project_errors = message_manager.get_formatted_messages()
        if project_errors:
            error_messages.append(f"#### {project.name}\n")
            error_messages.append(project_errors)
        message_manager.clear_messages()
    logger.info("All projects handled")
    if error_messages:
        logger.warning("Collected errors")
        config.error_messages_file_path.write_bytes("\n".join(error_messages).encode())


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception("Unhandled exception in sltt:")
        sys.exit(1)
