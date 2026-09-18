# Shows open listening ports

from commands.common import run_program


TITLE = "Listening ports"
DESCRIPTION = "Show services waiting for network connections"
ALIASES = {"connections", "ports", "ss"}


def run():
    print("Services listening for connections:\n")
    run_program(["ss", "-tuln"])