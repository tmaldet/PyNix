# Looks up a website with dig

from commands.common import ask_host, run_program


TITLE = "Look up DNS"
DESCRIPTION = "Find the IP addresses for a website"
ALIASES = {"dns", "dig", "lookup"}


def run():
    host = ask_host()
    if host is None:
        return

    print(f"\nLooking up addresses for {host}...\n")
    run_program(["dig", "+short", host])