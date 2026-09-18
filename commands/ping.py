# Pings a website or IP address

from commands.common import ask_host, run_program


TITLE = "Ping a host"
DESCRIPTION = "Check whether a website or device responds"
ALIASES = {"ping"}


def run():
    host = ask_host()
    if host is None:
        return

    print(f"\nChecking whether {host} responds (4 attempts)...\n")
    run_program(["ping", "-c", "4", host])