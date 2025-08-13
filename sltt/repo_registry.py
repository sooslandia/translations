from pathlib import Path

import git


class RepoRegistry:
    def __init__(self):
        self._repos = {}

    def get_repo(self, repo_path: Path) -> git.Repo:
        if repo := self._repos.get(repo_path):
            return repo
        repo = git.Repo(repo_path)
        self._repos[repo_path] = repo
        return repo


repo_registry = RepoRegistry()
