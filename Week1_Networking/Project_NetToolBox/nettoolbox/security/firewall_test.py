# nettoolbox/security/firewall_test.py
import socket
import time
from datetime import datetime

def test_firewall(host: str, ports=None, timeout: float = 2.0) -> dict:
    """
    Quick firewall / accessibility check:
    - Try connecting to common management ports (22, 3389, 80, 443) or user-specified ports.
    - This is a heuristic to see if ports are reachable (not a true firewall ruleset dump).
    """
    start = time.time()
    if ports is None:
        ports = [22, 3389, 80, 443]
    results = {}
    for port in ports:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                results[port] = "open"
        except Exception as e:
            results[port] = f"closed/unreachable ({e})"
    return {
        "test": "security.firewall_quick",
        "target": host,
        "success": True,
        "output": results,
        "error": None,
        "duration": time.time() - start,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
