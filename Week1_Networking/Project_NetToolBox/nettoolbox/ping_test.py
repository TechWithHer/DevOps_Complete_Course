# NetToolBox/ping_test.py
import platform
import subprocess

def run(target):
    """
    Run a ping test against the given IP/hostname.
    Returns a dictionary with success, latency, and raw output.
    """
    system = platform.system().lower()

    if system == "windows":
        cmd = ["ping", "-n", "4", target]
    else:
        cmd = ["ping", "-c", "4", target]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        output = result.stdout

        # Determine success
        success = "0% packet loss" in output or "Received = 4" in output

        # Attempt to extract latency
        latency = None
        try:
            if system != "windows":
                # Linux/macOS: rtt min/avg/max/mdev = 23.456/24.789/26.123/1.234 ms
                line = [l for l in output.splitlines() if "rtt min/avg" in l]
                if line:
                    latency = line[0].split("/")[4-3] + " ms"
            else:
                # Windows: Average = XXms
                line = [l for l in output.splitlines() if "Average" in l]
                if line:
                    latency = line[0].split("Average =")[-1].strip()
        except Exception:
            latency = None

        return {
            "test": "Ping",
            "target": target,
            "success": success,
            "latency": latency,
            "raw_output": output
        }

    except subprocess.TimeoutExpired:
        return {
            "test": "Ping",
            "target": target,
            "success": False,
            "latency": None,
            "error": "Ping command timed out"
        }

