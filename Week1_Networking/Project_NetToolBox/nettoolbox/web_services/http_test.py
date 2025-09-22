# nettoolbox/web_services/http_test.py
import requests
import time
from datetime import datetime
from urllib.parse import urlparse

def test_http(url: str, timeout: float = 5.0) -> dict:
    """
    Simple HTTP(S) GET. Returns status, headers summary.
    """
    start = time.time()
    try:
        resp = requests.get(url, timeout=timeout)
        headers = {k: resp.headers.get(k) for k in ("content-type", "server", "content-length")}
        return {
            "test": "web_services.http",
            "target": url,
            "success": True,
            "output": {"status_code": resp.status_code, "headers": headers},
            "error": None,
            "duration": time.time() - start,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
    except Exception as e:
        return {
            "test": "web_services.http",
            "target": url,
            "success": False,
            "output": None,
            "error": str(e),
            "duration": time.time() - start,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
