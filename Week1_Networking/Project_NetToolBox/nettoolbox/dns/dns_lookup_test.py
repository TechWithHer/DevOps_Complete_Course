# nettoolbox/dns/dns_lookup_test.py
import socket
import time
from datetime import datetime

def test_dns_lookup(domain: str) -> dict:
    start = time.time()
    try:
        ip = socket.gethostbyname(domain)
        result = {"test": "dns.lookup", "target": domain, "success": True, "output": ip, "error": None}
    except Exception as e:
        result = {"test": "dns.lookup", "target": domain, "success": False, "output": None, "error": str(e)}
    result["duration"] = time.time() - start
    result["timestamp"] = datetime.utcnow().isoformat() + "Z"
    return result
