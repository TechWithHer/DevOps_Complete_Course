# commands/dns_tools.py

import subprocess
from main import get_input, save_output

def run():
    print("\n🌐 DNS & Domain Tools")
    print("1) nslookup")
    print("2) dig")
    print("3) whois")
    print("4) host")
    print("5) hostname")
    print("6) Back to Main Menu")

    choice = get_input("Select tool: ")

    if choice == "1":
        target = get_input("Enter domain for nslookup: ")
        output = subprocess.getoutput(f"nslookup {target}")
        print(output)
        save_output("nslookup", target, output)

    elif choice == "2":
        target = get_input("Enter domain for dig: ")
        output = subprocess.getoutput(f"dig {target}")
        print(output)
        save_output("dig", target, output)

    elif choice == "3":
        target = get_input("Enter domain/IP for whois: ")
        output = subprocess.getoutput(f"whois {target}")
        print(output)
        save_output("whois", target, output)

    elif choice == "4":
        target = get_input("Enter domain for host: ")
        output = subprocess.getoutput(f"host {target}")
        print(output)
        save_output("host", target, output)

    elif choice == "5":
        output = subprocess.getoutput("hostname")
        print(output)
        save_output("hostname", "local", output)

    else:
        return
