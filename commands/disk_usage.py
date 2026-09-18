# Shows the disk space

from commands.common import run_program


TITLE = "Disk space"
DESCRIPTION = "Show free and used storage space"
ALIASES = {"disk", "storage", "df"}


def run():
    print("Disk space:\n")
    run_program(["df", "-h"])