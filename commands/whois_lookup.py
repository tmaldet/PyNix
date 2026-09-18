# Looks up public domain information

from commands.common import ask_host, run_program


TITLE = "WHOIS lookup"
DESCRIPTION = "Show public registration details for a domain"
ALIASES = {"whois"}


def run():
    host = ask_host()
    if host is None:
        return

    print(f"\nLooking up public information for {host}...\n")
    run_program(["whois", host])