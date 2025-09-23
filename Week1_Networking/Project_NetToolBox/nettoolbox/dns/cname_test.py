# nettoolbox/dns/cname_test.py
import dns.resolver
import time
from datetime import datetime

def test_cname(domain: str, timeout: float = 3.0) -> dict:
    start = time.time()
    try:
        answers = dns.resolver.resolve(domain, "CNAME", lifetime=timeout)
        records = [str(r.target) for r in answers]
        result = {"test": "dns.cname", "target": domain, "success": True, "output": records, "error": None}
    except Exception as e:
        result = {"test": "dns.cname", "target": domain, "success": False, "output": None, "error": str(e)}
    result["duration"] = time.time() - start
    result["timestamp"] = datetime.utcnow().isoformat() + "Z"
    return result

