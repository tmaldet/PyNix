# Shows running programs

from commands.common import run_program


TITLE = "Running processes"
DESCRIPTION = "Show programs that are currently running"
ALIASES = {"processes", "process", "ps"}


def run():
    print("Running processes:\n")
    run_program(["ps", "aux"])