# nettoolbox/web_services/api_test.py
import requests
import time
from datetime import datetime

def test_api(url: str, timeout: float = 5.0, method: str = "GET") -> dict:
    start = time.time()
    try:
        method = method.upper()
        resp = requests.request(method, url, timeout=timeout)
        snippet = None
        try:
            snippet = resp.json()
        except Exception:
            snippet = resp.text[:500]
        return {
            "test": "web_services.api",
            "target": url,
            "success": True,
            "output": {"status_code": resp.status_code, "body_snippet": snippet},
            "error": None,
            "duration": time.time() - start,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
    except Exception as e:
        return {
            "test": "web_services.api",
            "target": url,
            "success": False,
            "output": None,
            "error": str(e),
            "duration": time.time() - start,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
