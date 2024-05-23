from .command_line_arguments import CommandLineArguments


def main_cli():
    """ gdextension-cli Main entry point

    new
    ---
    project name : string
    from-git (default with template repository)
        repository-url : url
    from-local
        path : path

    build
    -----
    project path : path
    """
    args = CommandLineArguments().parse()
    print(args)
