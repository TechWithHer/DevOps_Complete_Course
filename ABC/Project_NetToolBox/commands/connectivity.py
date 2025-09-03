import subprocess

def check_connectivity():
    host = input("Enter the host to ping (default: 8.8.8.8): ") or "8.8.8.8"
    try:
        subprocess.run(["ping", "-c", "4", host], check=True)
    except subprocess.CalledProcessError:
        print("Ping failed. Host may be unreachable.")
