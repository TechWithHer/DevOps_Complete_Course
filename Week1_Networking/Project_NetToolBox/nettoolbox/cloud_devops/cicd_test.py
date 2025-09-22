# nettoolbox/cloud_devops/cicd_test.py
import socket
import time
from datetime import datetime

def test_cicd(target: str, timeout: float = 3.0) -> dict:
    """
    Minimal CI/CD connectivity check:
    - Try TLS TCP connect to target (e.g., github.com:443) to verify reachability.
    - `target` can be host or host:port. If port missing, default 443.
    """
    start = time.time()
    host = target
    port = 443
    if ":" in target:
        host, port_raw = target.rsplit(":", 1)
        try:
            port = int(port_raw)
        except:
            port = 443

    try:
        sock = socket.create_connection((host, port), timeout)
        sock.close()
        success = True
        output = f"Connected to {host}:{port}"
        error = None
    except Exception as e:
        success = False
        output = None
        error = str(e)

    return {
        "test": "cloud_devops.cicd",
        "target": target,
        "success": success,
        "output": output,
        "error": error,
        "duration": time.time() - start,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
