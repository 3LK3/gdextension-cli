"""
Simple script to create a new tag that triggers a release.
"""

import subprocess

from gdextension_cli import __version__

if __name__ == "__main__":
    version = __version__.__version__
    production_release = input("Do you want to create a production release? (yes/no): ")
    production_release = True if production_release == "yes" else False

    tag_message = input("Tag message (default: '%s'): " % version)
    if tag_message.strip() == "":
        tag_message = version

    # tags starting with 'release-' will trigger production release
    tag_name = "release-%s" % version
    if not production_release:
        # starting with 'test-release-' trigger test release to test.pypi
        tag_name = "test-%s" % tag_name

    print("Creating release %s" % version)
    print("With tag: %s" % tag_name)
    print("With tag message: '%s'" % tag_message)

    confirm = input("Are you sure? (yes/no): ")
    if confirm == "yes":
        subprocess.run(["git", "tag", "-a", tag_name, "-m", tag_message])
        subprocess.run(["git", "push", "--follow-tags"])
