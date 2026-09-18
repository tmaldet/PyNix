# Shows devices on the local network

from commands.common import run_program


TITLE = "Nearby devices"
DESCRIPTION = "Show devices already seen on your local network"
ALIASES = {"neighbors", "neighbours", "arp"}


def run():
    print("Devices this computer has seen on the local network:\n")
    run_program(["ip", "neighbor", "show"])