"""
Contains the commands available for a GDExtension project
"""

import glob
import logging
import shutil

from .project_options import CreateFromLocalPathOptions
from .template_renderer import TemplateRenderer, get_template_data

TEMPLATE_FILE_EXTENSION = ".tmpl"


def create_from_local_path(options: CreateFromLocalPathOptions):
    """
    Creates new GDExtension project from a local directory.
    :param options: Options for the creation of the new project.
    """
    logging.info("Creating new project '%s'", options.project_name)
    logging.info("Project path: %s", options.project_path)
    logging.info("Godot version: %s", options.godot_version)
    logging.info("Template path: %s", options.template_path)

    if not options.template_path.exists():
        raise FileNotFoundError(f"Template path not found: {options.template_path}")

    if not options.project_path.exists():
        logging.debug("Creating project directory at %s", options.project_path)
        options.project_path.mkdir(parents=True)

    _copy_non_template_files(options)
    _copy_templates(options)


def _copy_templates(options: CreateFromLocalPathOptions):
    """
    Copies all template files from template_path to project_path.
    Template files are all files with the extension '.tmpl'.
    :param options: Options for the creation of the new project.
    """
    logging.info("Copying template files ...")
    template_files = glob.glob(
        f"**/*{TEMPLATE_FILE_EXTENSION}", root_dir=options.template_path, recursive=True
    )
    template_renderer = TemplateRenderer(
        options.template_path, get_template_data(options)
    )

    for file in template_files:
        source_file = options.template_path / file
        if source_file.is_dir():
            continue

        # Supports templated file names
        target_file = template_renderer.render_path(
            options.project_path / file, TEMPLATE_FILE_EXTENSION
        )
        if not target_file.parent.exists():
            logging.debug("Creating directory at %s", target_file.parent)
            target_file.parent.mkdir(parents=True)

        logging.info("Render template %s to %s", file, target_file)
        template_renderer.render_file(str(file), target_file)


def _copy_non_template_files(options: CreateFromLocalPathOptions):
    """
    Copies all non template files from template_path to project_path.
    Non template files are all file without the extension '.tmpl'.
    :param options: Options for the creation of the new project.
    """
    logging.info("Copying non template files ...")
    non_template_files = glob.glob(
        f"**/*[!{TEMPLATE_FILE_EXTENSION}]",
        root_dir=options.template_path,
        recursive=True,
    )

    for file in non_template_files:
        source_file = options.template_path / file
        if source_file.is_dir():
            continue

        target_file = options.project_path / file
        if not target_file.parent.exists():
            logging.debug("Creating directory at %s", target_file.parent)
            target_file.parent.mkdir(parents=True)

        logging.info("Copy file %s to %s", file, target_file)
        shutil.copy(source_file, target_file)
