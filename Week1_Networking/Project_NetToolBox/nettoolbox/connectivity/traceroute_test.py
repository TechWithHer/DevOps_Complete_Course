# nettoolbox/connectivity/traceroute_test.py
import subprocess
import platform
import time
from datetime import datetime

def _traceroute_cmd(host: str, max_hops: int = 30):
    system = platform.system().lower()
    if system == "windows":
        # tracert on Windows
        return ["tracert", "-h", str(max_hops), host]
    else:
        return ["traceroute", "-m", str(max_hops), host]

def test_traceroute(host: str, max_hops: int = 20, timeout: float = 10.0) -> dict:
    start = time.time()
    cmd = _traceroute_cmd(host, max_hops)
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=timeout)
        result = {"test": "connectivity.traceroute", "target": host, "success": True, "output": output.decode(errors="ignore"), "error": None}
    except subprocess.CalledProcessError as e:
        result = {"test": "connectivity.traceroute", "target": host, "success": False, "output": e.output.decode(errors="ignore") if e.output else None, "error": str(e)}
    except Exception as e:
        result = {"test": "connectivity.traceroute", "target": host, "success": False, "output": None, "error": str(e)}
    result["duration"] = time.time() - start
    result["timestamp"] = datetime.utcnow().isoformat() + "Z"
    return result

