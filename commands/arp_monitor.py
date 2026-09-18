from commands.common import run_program


TITLE = "Watch ARP changes"
DESCRIPTION = "Watch devices joining or changing on your network"
ALIASES = {"arp-watch", "arp-monitor"}


def run():
    print("Watching network neighbor changes. Press Ctrl+C to stop.\n")
    run_program(["ip", "monitor", "neighbor"])