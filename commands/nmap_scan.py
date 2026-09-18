# Runs a small Nmap scan

from commands.common import ask_host, run_program


TITLE = "Basic port scan"
DESCRIPTION = "Check the 100 most common ports with Nmap"
ALIASES = {"nmap", "scan"}


def run():
    print("Only scan a computer that you own or have permission to test.")
    permission = input("Do you have permission? (yes/no): ").strip().lower()
    if permission not in {"yes", "y"}:
        print("The scan was cancelled.")
        return

    host = ask_host()
    if host is None:
        return

    print(f"\nScanning the 100 most common ports on {host}...\n")
    run_program(["nmap", "--top-ports", "100", "-T3", host])