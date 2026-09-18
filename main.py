import os

from commands import (
    arp_clear,
    arp_monitor,
    connections,
    current_user,
    disk_usage,
    dns_lookup,
    file_hash,
    interfaces,
    login_history,
    neighbor_devices,
    nmap_scan,
    ping,
    processes,
    routes,
    setup_tools,
    system_info,
    trace_route,
    web_headers,
    whois_lookup,
)


command_list = (
    setup_tools,
    ping,
    trace_route,
    dns_lookup,
    interfaces,
    routes,
    connections,
    neighbor_devices,
    arp_monitor,
    arp_clear,
    system_info,
    current_user,
    processes,
    disk_usage,
    login_history,
    whois_lookup,
    web_headers,
    file_hash,
    nmap_scan,
)


def setup_terminal():
    # Sets up the terminal like the old PyNix
    if os.name == "nt":
        os.system("color 0A")
        os.system("title PyNix Terminal")
        os.system("cls")
    else:
        os.system("clear")
        os.system("printf '\033[0;32m'")
        os.system("printf '\033]0;PyNix Terminal\007'")


def find_command(user_choice):
    for number, command in enumerate(command_list, start=1):
        if user_choice == str(number) or user_choice in command.ALIASES:
            return command
    return None


def show_menu():
    print("=========================================================================")
    print(" ____        _   _ _      __  __")
    print("|  _ \\ _   _| \\ | (_)_  _|  \\/  | ___ _ __  _   _")
    print("| |_) | | | |  \\| | \\ \\/ / |\\/| |/ _ \\ '_ \\| | | |")
    print("|  __/| |_| | |\\  | |>  <| |  | |  __/ | | | |_| |")
    print("|_|    \\__, |_| \\_|_/_/\\_\\_|  |_|\\___|_| |_|\\__,_|")
    print("       |___/")
    print("=========================================================================")
    print("          WINDOWS FRONT END FOR WSL LINUX SECURITY COMMANDS")
    print("=========================================================================")
    for number, command in enumerate(command_list, start=1):
        print(f"[{number:02}] {command.TITLE:<20} :: {command.DESCRIPTION}")
    print("[H]  Help                 :: Show help")
    print("[Q]  Quit                 :: Close PyNix")
    print("=========================================================================")


def show_help():
    print("\nPick a number or type a command name.")
    print("PyNix will ask you for anything the command needs.")
    print("Only scan computers and networks that you own or have permission to test.")


def complete_setup():
    # Linux commands stay locked until setup is done
    if setup_tools.setup_is_complete():
        return True

    print("=========================================================================")
    print("                         SETUP REQUIRED")
    print("=========================================================================")
    print("PyNix needs WSL, Ubuntu, and its Linux tools before the menu can open.")
    return setup_tools.run()


def main():
    setup_terminal()

    if not complete_setup():
        print("\nSetup is not complete, so Linux commands are still locked.")
        print("Run PyNix again when you are ready to finish setup.")
        return

    while True:
        show_menu()
        user_choice = input("\n>>> ").strip().lower()

        if user_choice in {"q", "quit", "exit"}:
            print("Goodbye.")
            return
        if user_choice in {"h", "help", "?"}:
            show_help()
            continue

        command = find_command(user_choice)
        if command is None:
            print(f"Please enter 1-{len(command_list)}, h, or q.")
            continue

        print()
        command.run()
        input("\nPress Enter to return to the menu...")
        setup_terminal()


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye.")