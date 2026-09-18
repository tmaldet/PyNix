# Makes a SHA-256 hash for a file

import os

from commands.common import ask_required, run_program


TITLE = "Hash a file"
DESCRIPTION = "Create a SHA-256 fingerprint to check a file"
ALIASES = {"hash", "sha256", "sha256sum"}


def run():
    file_name = ask_required("Path to the file: ")
    if file_name is None:
        return
    if not os.path.isfile(file_name):
        print("That file could not be found.")
        return

    print("\nSHA-256 file fingerprint:\n")
    run_program(["sha256sum", "--", file_name])