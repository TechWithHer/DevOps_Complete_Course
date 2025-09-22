#!/usr/bin/env python3
"""
Main entry point for NetToolbox Project
"""
import sys
import subprocess
import importlib
import os
import logging
import json

# ===== Logging Setup =====
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "nettoolbox.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ===== Dependencies =====
PYTHON_PACKAGES = [
    ("requests", "requests"),
    ("speedtest_cli", "speedtest-cli")
]

def install_package(module_name, pip_name):
    """Install package if not already installed."""
    try:
        importlib.import_module(module_name)
        print(f"✅ '{module_name}' is already installed.")
    except ImportError:
        print(f"⚠️ '{module_name}' not found. Installing via pip...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
        print(f"✅ '{module_name}' installed successfully.")

def check_dependencies():
    """Check and install all Python dependencies."""
    for module_name, pip_name in PYTHON_PACKAGES:
        install_package(module_name, pip_name)

# ===== Import Test Modules from NetToolbox =====
def import_test_modules():
    try:
        from nettoolbox import dns_test, http_test, ping_test
        return dns_test, http_test, ping_test
    except ImportError as e:
        print(f"❌ Error importing NetToolbox modules: {e}")
        sys.exit(1)

# ===== Main Menu =====
def main_menu(target, dns_test, http_test, ping_test):
    while True:
        print("\n--- NetToolbox Menu ---")
        print("1. Ping Test")
        print("2. DNS Test")
        print("3. HTTP Test")
        print("4. Run All Tests")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            result = ping_test.run(target)
        elif choice == "2":
            result = dns_test.run(target)
        elif choice == "3":
            result = http_test.run(target)
        elif choice == "4":
            for test in [ping_test.run, dns_test.run, http_test.run]:
                res = test(target)
                print(res)
                logging.info(res)
            continue
        elif choice == "5":
            print("👋 Exiting NetToolbox.")
            sys.exit(0)
        else:
            print("⚠️ Invalid choice, try again.")
            continue

        print(json.dumps(result, indent=4))
        logging.info(result)

# ===== Entry Point =====
if __name__ == "__main__":
    print("🚀 Starting NetToolbox Project...")

    # Step 1: Check dependencies
    check_dependencies()

    # Step 2: Import modules
    dns_test, http_test, ping_test = import_test_modules()

    # Step 3: Get target IP/domain
    target = input("Enter IP or Domain to test: ").strip()
    if not target:
        print("❌ No target provided. Exiting.")
        sys.exit(1)

    # Step 4: Run main menu
    main_menu(target, dns_test, http_test, ping_test)
