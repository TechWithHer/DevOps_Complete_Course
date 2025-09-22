# nettoolbox/connectivity/tcp_udp_ping_test.py
import socket
import time
from datetime import datetime

def test_tcp_ping(host: str, port: int = 80, timeout: float = 3.0) -> dict:
    start = time.time()
    try:
        with socket.create_connection((host, port), timeout=timeout):
            result = {"test": "connectivity.tcp", "target": f"{host}:{port}", "success": True, "output": f"TCP connect succeeded to {host}:{port}", "error": None}
    except Exception as e:
        result = {"test": "connectivity.tcp", "target": f"{host}:{port}", "success": False, "output": None, "error": str(e)}
    result["duration"] = time.time() - start
    result["timestamp"] = datetime.utcnow().isoformat() + "Z"
    return result

def test_udp_ping(host: str, port: int = 53, timeout: float = 3.0) -> dict:
    """
    UDP 'ping' sends a small packet (no guarantee of reply). Useful for checking reachability to UDP port.
    """
    start = time.time()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        sock.sendto(b"ntt", (host, port))
        # attempt to receive any response (not guaranteed)
        try:
            data, addr = sock.recvfrom(1024)
            output = f"UDP response from {addr}: {data[:200]!r}"
        except socket.timeout:
            output = f"UDP packet sent (no response received within {timeout}s)"
        sock.close()
        result = {"test": "connectivity.udp", "target": f"{host}:{port}", "success": True, "output": output, "error": None}
    except Exception as e:
        result = {"test": "connectivity.udp", "target": f"{host}:{port}", "success": False, "output": None, "error": str(e)}
    result["duration"] = time.time() - start
    result["timestamp"] = datetime.utcnow().isoformat() + "Z"
    return result
