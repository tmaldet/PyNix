# Traces the path to a website or IP

from commands.common import ask_host, run_program


TITLE = "Trace a route"
DESCRIPTION = "Show the path taken to a website or device"
ALIASES = {"trace", "traceroute"}


def run():
    host = ask_host()
    if host is None:
        return

    print(f"\nTracing the network path to {host}...\n")
    run_program(["traceroute", host])