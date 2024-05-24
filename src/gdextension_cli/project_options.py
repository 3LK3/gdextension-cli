"""
Contains options for project commands.
"""

import pathlib


class CreateProjectOptions:
    """Options for creating a new project."""

    project_name: str
    project_path: pathlib.Path
    godot_version: str

    def __init__(
        self, project_name: str, project_path: pathlib.Path, godot_version: str
    ):
        self.project_name = project_name
        self.project_path = project_path
        self.godot_version = godot_version


class CreateFromLocalPathOptions(CreateProjectOptions):
    """Options for creating a new project from a local folder."""

    template_path: pathlib.Path

    def __init__(
        self,
        project_name: str,
        project_path: pathlib.Path,
        godot_version: str,
        template_path: pathlib.Path,
    ):
        super().__init__(project_name, project_path, godot_version)
        self.template_path = template_path


class CreateFromGitOptions(CreateProjectOptions):
    """Options for creating a new project from a git repository."""

    template_repository_url: str

    def __init__(
        self,
        project_name: str,
        project_path: pathlib.Path,
        godot_version: str,
        template_repository_url: str,
    ):
        super().__init__(project_name, project_path, godot_version)
        self.template_repository_url = template_repository_url
