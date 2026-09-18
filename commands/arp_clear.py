from commands.common import run_program


TITLE = "Clear ARP cache"
DESCRIPTION = "Forget saved devices and learn them again"
ALIASES = {"arp-clear", "clear-arp"}


def run():
    print("This briefly clears the saved devices on this computer.")
    answer = input("Clear the ARP cache? (yes/no): ").strip().lower()
    if answer not in {"yes", "y"}:
        print("The command was cancelled.")
        return

    print("\nClearing the ARP cache...\n")
    run_program(["sudo", "ip", "neighbor", "flush", "all"])