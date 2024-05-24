"""
gdextension_cli entry point with callable function main_cli()
"""

import logging
from pathlib import Path

from .command_line_args import CommandLineArgs
from .project import create_from_local_path
from .project_options import CreateFromLocalPathOptions


def main_cli():
    """gdextension-cli main entry point used in pyproject.toml"""
    arguments = CommandLineArgs().create().parse()
    initialize_logging(arguments.verbose)

    print(arguments)  # FIXME remove later

    match arguments.subcommand:
        case "new":
            if arguments.from_local:
                _new_project_from_local(arguments)
            elif arguments.from_git:
                _new_project_from_git(arguments)
            else:
                raise AssertionError(
                    "Expected arguments '--from-local' or '--from-git'"
                )
        case "build":
            print("BUILD")
        case _:
            raise ValueError(f"Unknown subcommand: {arguments.subcommand}")


def _new_project_from_git(args):
    """
    Runs the create project command based on given arguments.
    :param args: Command line arguments
    """
    pass


def _new_project_from_local(args):
    """
    Runs the create project command based on given arguments.
    :param args: Command line arguments
    """
    options = CreateFromLocalPathOptions(
        args.name,
        args.output_path if args.output_path else Path.cwd() / args.name,
        args.godot_version,
        args.from_local,
    )
    create_from_local_path(options)


def initialize_logging(verbose: bool):
    """
    Initializes the logging module with a log level based on the given verbose argument.
    :param verbose: DEBUG if True, otherwise INFO
    """
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(levelname)s - %(message)s",
    )
