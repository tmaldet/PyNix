import ipaddress
import os
import re
import shutil
import subprocess


HOSTNAME_PATTERN = re.compile(
    r"^(?=.{1,253}\.?$)(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)*"
    r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.?$"
)


def wsl_is_ready():
    # WSL needs a Linux distro before it can run commands
    if os.name != "nt":
        return True
    if shutil.which("wsl") is None:
        return False

    check = subprocess.run(
        ["wsl", "uname"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return check.returncode == 0


def run_program(arguments):
    # Windows sends the Linux command through WSL
    program = arguments[0]
    run_command = list(arguments)

    if os.name == "nt":
        if not wsl_is_ready():
            print("WSL does not have a working Linux distro yet.")
            print("Open PowerShell as Administrator and run:")
            print("wsl --install -d Ubuntu")
            print("Restart if asked, then open Ubuntu once to finish setup.")
            return False
        run_command = ["wsl"] + run_command
    elif shutil.which(program) is None:
        print(f"'{program}' is not installed on this computer.")
        print("Install it with your Linux package manager, then try again.")
        return False

    try:
        completed = subprocess.run(run_command, check=False)
    except OSError as error:
        print(f"Could not start {program}: {error}")
        return False

    if completed.returncode != 0:
        print(f"\n{program} finished with exit code {completed.returncode}.")
        return False
    return True


def tool_is_installed(tool):
    # Checks inside WSL when PyNix is running on Windows
    if os.name == "nt":
        if not wsl_is_ready():
            return False
        check = subprocess.run(
            ["wsl", "which", tool],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        return check.returncode == 0
    return shutil.which(tool) is not None


def ask_required(prompt):
    value = input(prompt).strip()
    if not value:
        print("Nothing was entered, so the command was cancelled.")
        return None
    return value


def ask_host():
    # This makes sure the host is safe to use
    value = ask_required("Website name or IP address: ")
    if value is None:
        return None

    try:
        ipaddress.ip_address(value)
        return value
    except ValueError:
        if HOSTNAME_PATTERN.fullmatch(value):
            return value

    print("That does not look like a valid website name or IP address.")
    return None