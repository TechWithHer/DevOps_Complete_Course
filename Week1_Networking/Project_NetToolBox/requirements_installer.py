import subprocess
import shutil

def is_installed(command):
    return shutil.which(command) is not None

def install_package(package_name):
    try:
        subprocess.run(['sudo', 'apt', 'install', '-y', package_name], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}")

def ensure_dependencies():
    required_commands = {
        'ping': 'iputils-ping',
        'dig': 'dnsutils',
        'ifconfig': 'net-tools',
        'ip': 'iproute2',
        'netstat': 'net-tools',
        'ss': 'iproute2',
        'ufw': 'ufw',
        'curl': 'curl',
    }

    for command, package in required_commands.items():
        if not is_installed(command):
            print(f"Installing missing command: {command} ({package})")
            install_package(package)

if __name__ == "__main__":
    ensure_dependencies()
