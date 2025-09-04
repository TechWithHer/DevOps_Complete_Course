#!/usr/bin/env python3
"""
NetToolBox - Full CLI with all network tests
"""

import os
import sys
import logging
import requests

# Import all tests from NetToolBox package
from NetToolBox import (
    ping_test,
    traceroute_test,
    dns_test,
    port_scan,
    http_check,
    ssl_check
)

# ===== Logging Setup =====
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "nettoolbox.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ===== Helper: Get IP or Domain =====
def get_ip_or_domain():
    user_input = input("Enter IP or domain (leave blank for auto-detect): ").strip()
    if user_input:
        return user_input
    try:
        public_ip = requests.get("https://api.ipify.org").text
        print(f"🔹 Auto-detected Public IP: {public_ip}")
        return public_ip
    except Exception as e:
        print("❌ Failed to auto-detect IP. Please enter manually.")
        logging.error(f"IP detection failed: {e}")
        return None

# ===== Logging Function =====
def log_result(result):
    if result.get("success"):
        logging.info(f"{result['test']} succeeded for {result['target']}")
    else:
        logging.warning(f"{result['test']} failed for {result['target']} | Info: {result.get('error', 'Check manually')}")

# ===== Print Results Function =====
def print_test_result(result):
    print(f"\n--- {result['test']} Result ---")
    print(f"Target: {result['target']}")
    print(f"Success: {'✅' if result['success'] else '❌'}")

    # Ping Test
    if result.get("latency"):
        print(f"Latency: {result['latency']}")
    # DNS Test
    if result.get("ip_address"):
        print(f"Resolved IP: {result['ip_address']}")
    if result.get("reverse_domain"):
        print(f"Reverse Domain: {result['reverse_domain']}")
    # Port Scan
    if result.get("open_ports"):
        print("Open Ports:")
        for p in result["open_ports"]:
            print(f"  - {p}")
    # HTTP Check
    if result.get("results"):
        for r in result["results"]:
            status = "✅" if r["success"] else "❌"
            print(f"{r['url']} -> Status: {r['status_code']}, Time: {r['response_time_ms']}ms {status}")
            if r.get("error"):
                print(f"  Error: {r['error']}")
    # SSL Check
    if result.get("issuer"):
        print(f"Issuer: {result['issuer']}")
    if result.get("expiry_date"):
        print(f"Expiry Date: {result['expiry_date']}")
    if result.get("error"):
        print(f"Error: {result['error']}")

# ===== Menu =====
def main_menu(target):
    while True:
        print("\n--- NetToolBox Menu ---")
        print("1. Ping Test")
        print("2. Traceroute")
        print("3. DNS Resolution")
        print("4. Port Scan")
        print("5. HTTP/HTTPS Check")
        print("6. SSL/TLS Certificate Check")
        print("7. Run All Tests")
        print("8. Exit")

        choice = input("Select an option (1-8): ").strip()

        if choice == "1":
            result = ping_test.run(target)
        elif choice == "2":
            result = traceroute_test.run(target)
        elif choice == "3":
            result = dns_test.run(target)
        elif choice == "4":
            result = port_scan.run(target)
        elif choice == "5":
            result = http_check.run(target)
        elif choice == "6":
            result = ssl_check.run(target)
        elif choice == "7":
            all_results = []
            for test in [ping_test.run, traceroute_test.run, dns_test.run, port_scan.run, http_check.run, ssl_check.run]:
                res = test(target)
                log_result(res)
                print_test_result(res)
                all_results.append(res)
            continue
        elif choice == "8":
            print("👋 Exiting NetToolBox. Goodbye!")
            sys.exit(0)
        else:
            print("⚠️ Invalid choice, try again.")
            continue

        log_result(result)
        print_test_result(result)

# ===== Entry Point =====
if __name__ == "__main__":
    print("🚀 Welcome to NetToolBox - DevOps Network Testing CLI")
    target = get_ip_or_domain()
    if target:
        main_menu(target)
    else:
        print("❌ No valid target provided. Exiting.")
        sys.exit(1)

