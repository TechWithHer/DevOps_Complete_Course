# NetToolBox/dns_test.py
import socket

def run(target):
    """
    Performs forward and reverse DNS resolution on the given IP/domain.
    Returns a dictionary with success and resolved addresses.
    """
    try:
        # Forward lookup (domain → IP)
        ip_address = socket.gethostbyname(target)

        # Reverse lookup (IP → domain)
        try:
            reverse_domain = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            reverse_domain = "Reverse lookup failed"

        success = True
        return {
            "test": "DNS Resolution",
            "target": target,
            "success": success,
            "ip_address": ip_address,
            "reverse_domain": reverse_domain
        }

    except socket.gaierror as e:
        return {
            "test": "DNS Resolution",
            "target": target,
            "success": False,
            "error": f"DNS resolution failed: {e}"
        }

