import argparse
import pathlib


class CommandLineArguments:
    def __init__(self):
        self._parser = argparse.ArgumentParser(prog="gdextension-cli")
        subcommands = self._parser.add_subparsers(
            help="Choose a sub command", required=True
        )

        new_parser = subcommands.add_parser("new")
        new_parser.add_argument("name", type=str, help="Name of the new project")
        new_parser.add_argument(
            "-g",
            "--godot-version",
            type=str,
            help="Godot version and branch name for template repositories",
        )

        from_group = new_parser.add_mutually_exclusive_group(required=False)
        from_group.add_argument(
            "--from-git",
            metavar="GIT_URL",
            type=str,
            required=False,
            default="https://github.com/3LK3/gdextension-template.git",
            help="URL of a project template repository",
        )
        from_group.add_argument(
            "--from-local",
            metavar="PATH",
            type=pathlib.Path,
            required=False,
            help="Path to a local folder containing a project template",
        )

        # from_subcommands = new_parser.add_subparsers(required=False)
        #
        # from_git_parser = from_subcommands.add_parser(
        #     "from-git",
        #     help="Create project using a project template from a git repository",
        # )
        # from_git_parser.add_argument(
        #     "-u",
        #     "--url",
        #     type=str,
        #     required=True,
        #     default="https://github.com/3LK3/gdextension-template.git",
        #     help="URL of a project template repository",
        # )
        #
        # from_local_parser = from_subcommands.add_parser(
        #     "from-local",
        #     help="Create project using a project template from a local folder",
        # )
        # from_local_parser.add_argument(
        #     "-p",
        #     "--path",
        #     type=pathlib.Path,
        #     help="Path to a local folder containing a project template",
        # )

        build_parser = subcommands.add_parser("build")
        build_parser.add_argument("path", type=str, help="Path of the project to build")

    def parse(self) -> argparse.Namespace:
        return self._parser.parse_args()
