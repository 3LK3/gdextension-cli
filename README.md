# gdextension-cli

A command line interface for Godot's GDExtension.

My intention with this tool was to create an automated way to create a C++ based GDExtension
project. The process behind `gdextension-cli new <NAME>` is
based [Godot's GDExtension documentation](https://docs.godotengine.org/en/stable/tutorials/scripting/gdextension/gdextension_cpp_example.html).

Therefore, this tool implements a templating mechanism to create projects from a git repository or
a local directory. By default, the `new` command uses https://github.com/3LK3/gdextension-template
as the template. You can also [use your own repository](#from-a-custom-git-repository).

## Requirements

- Python >= 3.8
- Git
- SCons
    - you will most likely need SCons to build your extension anyway. But since you have python
      installed, you can install SCons via `pip install scons`

## Installation

`pip install gdextension-cli`

## Usage

### Create a new project

`gdextension-cli new <NAME>`

This will create a project called <NAME> in a new directory relative to your current path.

By default, https://github.com/3LK3/gdextension-template is used as the project template.

#### From a custom git repository

You can also use your own template repository to create a new project.

`gdextension-cli new <NAME> --from-git https://github.com/<you>/<your-custom-template>`

#### From a local directory

If you have a template on your local file system you can also create a project from there.

`gdextension-cli new <NAME> --from-local /home/you/your_template`