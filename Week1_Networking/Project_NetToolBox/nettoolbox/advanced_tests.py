import subprocess
import requests
import socket
import ssl
import datetime
import shutil
import sys

# --------------------------
# Bandwidth Test
# --------------------------
def bandwidth_test():
    if shutil.which("speedtest-cli") is None:
        return "speedtest-cli not installed. Install with: pip install speedtest-cli"
    try:
        result = subprocess.check_output(["speedtest-cli", "--simple"]).decode()
        return result
    except Exception as e:
        return f"Error running bandwidth test: {e}"

# --------------------------
# API Rate Limit Test (GitHub example)
# --------------------------
def api_rate_limit_test():
    try:
        response = requests.get("https://api.github.com/rate_limit")
        if response.status_code == 200:
            return response.json()
        else:
            return f"API returned status {response.status_code}"
    except Exception as e:
        return f"Error checking API rate limit: {e}"

# --------------------------
# SSL Certificate Expiry Test
# --------------------------
def ssl_expiry_test(host, port=443):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                exp_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                days_left = (exp_date - datetime.datetime.utcnow()).days
                return f"SSL certificate for {host} expires in {days_left} days"
    except Exception as e:
        return f"Error checking SSL expiry: {e}"

# --------------------------
# Package Registry Connectivity Tests
# --------------------------
def pip_registry_test():
    try:
        response = requests.get("https://pypi.org/simple/requests/")
        return "PyPI reachable" if response.status_code == 200 else f"PyPI error {response.status_code}"
    except Exception as e:
        return f"Error reaching PyPI: {e}"


def npm_registry_test():
    try:
        response = requests.get("https://registry.npmjs.org/express")
        return "NPM registry reachable" if response.status_code == 200 else f"NPM error {response.status_code}"
    except Exception as e:
        return f"Error reaching NPM registry: {e}"

# --------------------------
# Docker Registry Connectivity Test
# --------------------------
def docker_registry_test():
    try:
        response = requests.get("https://registry-1.docker.io/v2/")
        if response.status_code == 200:
            return "Docker Hub reachable"
        elif response.status_code == 401:
            return "Docker Hub reachable (auth required)"
        else:
            return f"Docker Hub error {response.status_code}"
    except Exception as e:
        return f"Error reaching Docker Hub: {e}"

# --------------------------
# Firewall Rules Check (Linux iptables)
# --------------------------
def firewall_rules_check():
    try:
        result = subprocess.check_output(["iptables", "-L"]).decode()
        return result
    except Exception as e:
        return f"Error checking firewall rules: {e}"

# --------------------------
# Latency & Packet Loss Test
# --------------------------
def latency_test(host="8.8.8.8", count=5):
    try:
        result = subprocess.check_output(["ping", "-c", str(count), host]).decode()
        return result
    except Exception as e:
        return f"Error running ping test: {e}"


if __name__ == "__main__":
    print("=== Advanced Network Tests ===")
    print("\n[ Bandwidth Test ]\n", bandwidth_test())
    print("\n[ API Rate Limit Test ]\n", api_rate_limit_test())
    print("\n[ SSL Expiry Test (github.com) ]\n", ssl_expiry_test("github.com"))
    print("\n[ PyPI Registry Test ]\n", pip_registry_test())
    print("\n[ NPM Registry Test ]\n", npm_registry_test())
    print("\n[ Docker Registry Test ]\n", docker_registry_test())
    print("\n[ Firewall Rules ]\n", firewall_rules_check())
    print("\n[ Latency Test ]\n", latency_test())

