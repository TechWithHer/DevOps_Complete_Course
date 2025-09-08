import os
import subprocess
import socket
import json
import datetime
import requests
import ssl
import urllib.parse

LOG_FILE = "logs/network_checks.log"

def log_result(check_name, target, result):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {check_name} - Target: {target} - Result: {result}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def save_json(results, filename="logs/network_results.json"):
    os.makedirs("logs", exist_ok=True)
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

# --------------------- HOST & CONNECTIVITY CHECKS --------------------- #
def ping_test(host):
    try:
        output = subprocess.check_output(["ping", "-c", "4", host], universal_newlines=True)
        log_result("Ping Test", host, "Success")
        return output
    except subprocess.CalledProcessError:
        log_result("Ping Test", host, "Failed")
        return "Ping failed"

def traceroute_test(host):
    try:
        output = subprocess.check_output(["traceroute", host], universal_newlines=True)
        log_result("Traceroute Test", host, "Success")
        return output
    except subprocess.CalledProcessError:
        log_result("Traceroute Test", host, "Failed")
        return "Traceroute failed"

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        log_result("DNS Resolution", domain, ip)
        return ip
    except socket.gaierror:
        log_result("DNS Resolution", domain, "Failed")
        return "DNS resolution failed"

def reverse_dns(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        log_result("Reverse DNS", ip, hostname)
        return hostname
    except socket.herror:
        log_result("Reverse DNS", ip, "Failed")
        return "Reverse DNS failed"

# --------------------- PORT & SERVICE CHECKS --------------------- #
def port_check(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        result = sock.connect_ex((host, port))
        status = "Open" if result == 0 else "Closed"
        log_result("Port Check", f"{host}:{port}", status)
        return status
    except Exception as e:
        log_result("Port Check", f"{host}:{port}", f"Failed ({e})")
        return f"Failed ({e})"
    finally:
        sock.close()

def ssl_check(host):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
        log_result("SSL Check", host, "Valid")
        return cert
    except Exception as e:
        log_result("SSL Check", host, f"Failed ({e})")
        return f"SSL check failed ({e})"

# --------------------- HTTP/HTTPS CHECKS --------------------- #
def http_check(url):
    try:
        response = requests.get(url, timeout=5)
        data = {
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds(),
            "content_snippet": response.text[:100]  # first 100 chars
        }
        log_result("HTTP Check", url, f"{data}")
        return data
    except requests.RequestException as e:
        log_result("HTTP Check", url, f"Failed ({e})")
        return f"HTTP check failed ({e})"

# --------------------- NETWORK INTERFACE / SYSTEM CHECKS --------------------- #
def interface_check():
    try:
        output = subprocess.check_output(["ip", "addr"], universal_newlines=True)
        log_result("Interface Check", "Local", "Success")
        return output
    except Exception as e:
        log_result("Interface Check", "Local", f"Failed ({e})")
        return f"Interface check failed ({e})"

def routing_table():
    try:
        output = subprocess.check_output(["ip", "route"], universal_newlines=True)
        log_result("Routing Table Check", "Local", "Success")
        return output
    except Exception as e:
        log_result("Routing Table Check", "Local", f"Failed ({e})")
        return f"Routing table check failed ({e})"

def firewall_rules():
    try:
        output = subprocess.check_output(["sudo", "iptables", "-L"], universal_newlines=True)
        log_result("Firewall Rules Check", "Local", "Success")
        return output
    except Exception as e:
        log_result("Firewall Rules Check", "Local", f"Failed ({e})")
        return f"Firewall check failed ({e})"

# --------------------- MAIN EXECUTION --------------------- #
if __name__ == "__main__":
    results = {}

    # Example usage:
    host = "google.com"
    domain = "google.com"
    ip = dns_lookup(domain)

    results["ping"] = ping_test(host)
    results["traceroute"] = traceroute_test(host)
    results["dns"] = ip
    results["reverse_dns"] = reverse_dns(ip)
    results["ports"] = {port: port_check(host, port) for port in [22, 80, 443, 3306]}
    results["ssl"] = ssl_check(host)
    results["http"] = http_check(f"https://{host}")
    results["interfaces"] = interface_check()
    results["routing"] = routing_table()
    results["firewall"] = firewall_rules()

    # Save results to JSON
    save_json(results)

    print("All checks completed. Logs and JSON saved in 'logs/' folder.")
