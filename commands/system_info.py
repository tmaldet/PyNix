# Shows Linux system information

from commands.common import run_program


TITLE = "System information"
DESCRIPTION = "Show the Linux version and computer details"
ALIASES = {"system", "uname"}


def run():
    print("Linux system information:\n")
    run_program(["uname", "-a"])