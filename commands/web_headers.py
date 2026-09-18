# Shows website headers

from commands.common import ask_host, run_program


TITLE = "Website headers"
DESCRIPTION = "Show basic information returned by a web server"
ALIASES = {"headers", "curl"}


def run():
    host = ask_host()
    if host is None:
        return

    website = "https://" + host
    print(f"\nRequesting headers from {website}...\n")
    run_program(["curl", "--head", "--location", "--max-time", "15", website])