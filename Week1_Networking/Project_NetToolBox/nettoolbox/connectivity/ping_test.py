# nettoolbox/connectivity/ping_test.py
import subprocess
import platform
import time
from datetime import datetime

def _get_ping_command(host: str, count: int = 1):
    # cross-platform: windows uses -n, unix uses -c
    system = platform.system().lower()
    if system == "windows":
        return ["ping", "-n", str(count), host]
    else:
        return ["ping", "-c", str(count), host]

def test_ping(host: str, count: int = 1, timeout: float = 3.0) -> dict:
    start = time.time()
    cmd = _get_ping_command(host, count)
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=timeout)
        result = {"test": "connectivity.ping", "target": host, "success": True, "output": output.decode(errors="ignore"), "error": None}
    except subprocess.CalledProcessError as e:
        result = {"test": "connectivity.ping", "target": host, "success": False, "output": e.output.decode(errors="ignore") if e.output else None, "error": str(e)}
    except Exception as e:
        result = {"test": "connectivity.ping", "target": host, "success": False, "output": None, "error": str(e)}
    result["duration"] = time.time() - start
    result["timestamp"] = datetime.utcnow().isoformat() + "Z"
    return result
