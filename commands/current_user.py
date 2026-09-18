# Shows the current user

from commands.common import run_program


TITLE = "Current user"
DESCRIPTION = "Show your username, user ID, and groups"
ALIASES = {"user", "whoami", "id"}


def run():
    print("Your user and group information:\n")
    run_program(["id"])