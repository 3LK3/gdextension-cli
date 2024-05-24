"""
Contains anything for rendering templates.
"""

import logging
from pathlib import Path
from typing import Dict

from jinja2 import Environment, FileSystemLoader

from .project_options import CreateFromLocalPathOptions


class TemplateRenderer:
    """Template renderer does what its name says."""

    environment: Environment
    data: Dict[str, str]

    def __init__(self, template_path, data: Dict[str, str]):
        logging.debug("Initializing template renderer ...")
        self.environment = Environment(loader=FileSystemLoader(template_path))
        self.data = data
        logging.debug("Using template data: %s", self.data)

    def render_path(self, path: Path, remove_extension: str | None = None) -> Path:
        result = self.environment.from_string(str(path)).render(self.data)
        if remove_extension is not None:
            result = result[: -len(remove_extension)]
        return Path(result)

    def render_file(self, file: str, output_file: Path):
        self.environment.get_template(file.replace("\\", "/")).stream(self.data).dump(
            str(output_file)
        )


def get_template_data(options: CreateFromLocalPathOptions) -> Dict[str, str]:
    return {
        "name": options.project_name,
        "lib_name": _get_library_name(options.project_name),
        "class_name": _get_class_name(options.project_name),
    }


def _get_library_name(project_name: str) -> str:
    return project_name.lower().replace("_", "")


def _get_class_name(project_name: str) -> str:
    class_name = ""
    for part in project_name.lower().split("_"):
        class_name += part.capitalize()
    return class_name
