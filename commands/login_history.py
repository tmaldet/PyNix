# Shows recent logins

from commands.common import run_program


TITLE = "Login history"
DESCRIPTION = "Show the 10 most recent user logins"
ALIASES = {"logins", "last"}


def run():
    print("Recent user logins:\n")
    run_program(["last", "-n", "10"])