# nettoolbox/cloud_devops/kubernetes_test.py
import socket
import subprocess
import time
from datetime import datetime

def test_kubernetes(api_server: str, port: int = 6443, timeout: float = 3.0) -> dict:
    """
    Minimal Kubernetes test:
    - Attempt TCP connection to api_server:port (default 6443).
    - Check if 'kubectl' binary is available on the host via subprocess (client).
    """
    start = time.time()
    result = {"test": "cloud_devops.kubernetes", "target": f"{api_server}:{port}"}
    # TCP check
    try:
        sock = socket.create_connection((api_server, port), timeout)
        sock.close()
        result["connection"] = "reachable"
    except Exception as e:
        result["connection"] = "unreachable"
        result["connection_error"] = str(e)

    # kubectl check
    try:
        proc = subprocess.run(["kubectl", "version", "--client", "--short"], capture_output=True, text=True, timeout=5)
        if proc.returncode == 0:
            result["kubectl"] = proc.stdout.strip()
        else:
            result["kubectl"] = proc.stderr.strip() or "kubectl returned non-zero"
    except FileNotFoundError:
        result["kubectl"] = "kubectl not installed or not in PATH"
    except Exception as e:
        result["kubectl"] = f"kubectl check error: {e}"

    result["success"] = result.get("connection") == "reachable"
    result["duration"] = time.time() - start
    result["timestamp"] = datetime.utcnow().isoformat() + "Z"
    return result
