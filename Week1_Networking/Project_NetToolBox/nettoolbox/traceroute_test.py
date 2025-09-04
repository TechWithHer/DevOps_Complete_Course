# NetToolBox/traceroute_test.py
import platform
import subprocess

def run(target):
    """
    Run a traceroute (or tracert on Windows) to the target IP/domain.
    Returns a dictionary with success and raw output.
    """
    system = platform.system().lower()

    if system == "windows":
        cmd = ["tracert", target]
    else:
        cmd = ["traceroute", target]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        output = result.stdout

        success = result.returncode == 0

        return {
            "test": "Traceroute",
            "target": target,
            "success": success,
            "raw_output": output
        }

    except subprocess.TimeoutExpired:
        return {
            "test": "Traceroute",
            "target": target,
            "

