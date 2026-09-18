# PyNix

PyNix is a Python terminal that lets you use Linux commands on Windows.
It uses WSL to run the commands.

## What It Can Do

- Ping websites and IP addresses
- Look up DNS and WHOIS information
- Show IP addresses, routes, ports, and nearby devices
- Show system information, users, processes, disks, and logins
- Watch ARP changes and clear the local ARP cache
- Hash files with SHA-256
- Scan the 100 most common ports with Nmap

## How To Start

1. Install Python 3.9 or newer.
2. Open PowerShell in the PyNix folder.
3. Run this command:

```powershell
python main.py
```

PyNix checks if WSL, Ubuntu, and the Linux tools are installed. If something
is missing, it asks if you want to install it. You may need to run PowerShell
as Administrator or restart your computer.

If Ubuntu gets installed, open it once and make your Linux username. Then run
PyNix again.

## Using PyNix

Type a menu number or a command name. For example, type `ping`, `dns`, or
`ports`. Type `q` to quit.

Only scan computers and networks that you own or have permission to test.
ARP tools only see the WSL network, not the full Windows network.
sudo apt update

## THIS PROJECT HAS NOT BEEN TESTED IN YEARS
This was a project I made in 7th grade, I made some basic changes to make
the code easier to follow and understand, again this has not been tested
so the code may not work as intended.