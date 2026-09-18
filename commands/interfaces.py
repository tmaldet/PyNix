# Shows network cards and addresses

from commands.common import run_program


TITLE = "Network addresses"
DESCRIPTION = "Show this computer's network connections"
ALIASES = {"addresses", "interfaces", "ip"}


def run():
    print("Your network interfaces and addresses:\n")
    run_program(["ip", "-brief", "address"])