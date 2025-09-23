# nettoolbox/dns/mx_test.py
import dns.resolver
import time
from datetime import datetime

def test_mx(domain: str, timeout: float = 3.0) -> dict:
    start = time.time()
    try:
        answers = dns.resolver.resolve(domain, "MX", lifetime=timeout)
        records = [f"{r.exchange} (pref={r.preference})" for r in answers]
        result = {"test": "dns.mx", "target": domain, "success": True, "output": records, "error": None}
    except Exception as e:
        result = {"test": "dns.mx", "target": domain, "success": False, "output": None, "error": str(e)}
    result["duration"] = time.time() - start
    result["timestamp"] = datetime.utcnow().isoformat() + "Z"
    return result

print(test_mx("ayushisingh.com"))