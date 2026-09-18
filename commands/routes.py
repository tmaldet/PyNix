# Shows the routing table

from commands.common import run_program


TITLE = "Routing table"
DESCRIPTION = "Show where network traffic is sent"
ALIASES = {"route", "routes"}


def run():
    print("Your network routes:\n")
    run_program(["ip", "route", "show"])