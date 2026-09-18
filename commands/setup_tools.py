import os
import subprocess

from commands.common import run_program, tool_is_installed, wsl_is_ready


TITLE = "Install/check tools"
DESCRIPTION = "Install everything needed for every PyNix command"
ALIASES = {"install", "setup", "update"}

tool_packages = {
    "ping": "iputils-ping",
    "traceroute": "traceroute",
    "dig": "dnsutils",
    "ip": "iproute2",
    "ss": "iproute2",
    "ps": "procps",
    "whois": "whois",
    "curl": "curl",
    "nmap": "nmap",
}


def find_missing_tools():
    missing_tools = []
    for tool in tool_packages:
        if not tool_is_installed(tool):
            missing_tools.append(tool)
    return missing_tools


def setup_is_complete():
    if not wsl_is_ready():
        return False
    return len(find_missing_tools()) == 0


def install_ubuntu():
    # Starts the official Windows WSL installer
    print("\nWindows may ask for Administrator permission.")
    print("Installing WSL and Ubuntu...\n")
    try:
        install = subprocess.run(
            ["wsl", "--install", "-d", "Ubuntu"],
            check=False,
        )
    except OSError as error:
        print(f"Could not start the WSL installer: {error}")
        return False

    if install.returncode != 0:
        print("The WSL installer could not finish.")
        print("Run PyNix as Administrator and try setup again.")
        return False

    print("\nUbuntu was requested from Windows.")
    print("Restart Windows if asked, then open Ubuntu once to create your user.")
    return wsl_is_ready()


def run():
    # Finds anything PyNix still needs
    if not wsl_is_ready():
        if os.name != "nt":
            print("PyNix could not find a working Linux system.")
            return False

        print("WSL or Ubuntu is not completely installed.")
        answer = input("Install WSL and Ubuntu now? (yes/no): ").strip().lower()
        if answer not in {"yes", "y"}:
            print("Installation cancelled.")
            return False
        if not install_ubuntu():
            return False

    missing_tools = find_missing_tools()
    if not missing_tools:
        print("Everything needed by PyNix is already installed!")
        return True

    print("These tools are missing:")
    print(", ".join(missing_tools))
    print("\nThis installer is made for Debian, Ubuntu, Kali, and Linux Mint.")
    answer = input("Install all missing tools now? (yes/no): ").strip().lower()
    if answer not in {"yes", "y"}:
        print("Installation cancelled.")
        return False

    packages = []
    for tool in missing_tools:
        package = tool_packages[tool]
        if package not in packages:
            packages.append(package)

    print("\nUpdating the package list...\n")
    if not run_program(["sudo", "apt-get", "update"]):
        return False

    print("\nInstalling the missing tools...\n")
    if not run_program(["sudo", "apt-get", "install", "-y"] + packages):
        return False

    print("\nSetup complete! All PyNix commands are unlocked.")
    return True