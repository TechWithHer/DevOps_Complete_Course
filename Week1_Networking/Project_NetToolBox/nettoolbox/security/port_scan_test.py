# nettoolbox/security/port_scan_test.py
import socket
import time
from datetime import datetime

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3389, 3306, 5432]

def test_port_scan(host: str, ports=None, timeout: float = 0.8) -> dict:
    start = time.time()
    if ports is None:
        ports = COMMON_PORTS
    open_ports = []
    for port in ports:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                open_ports.append(port)
        except:
            pass
    return {
        "test": "security.port_scan",
        "target": host,
        "success": True,
        "output": {"open_ports": open_ports},
        "error": None,
        "duration": time.time() - start,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
