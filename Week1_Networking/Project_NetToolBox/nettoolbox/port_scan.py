# NetToolBox/port_scan.py
import socket

# Common ports to scan
COMMON_PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    27017: "MongoDB"
}

def run(target, ports=None):
    """
    Scan the target for open ports.
    Returns a dictionary with open ports and status.
    """
    if ports is None:
        ports = COMMON_PORTS.keys()

    open_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(f"{port} ({COMMON_PORTS.get(port,'Unknown')})")
        except Exception:
            pass
        finally:
            sock.close()

    success = len(open_ports) > 0

    return {
        "test": "Port Scan",
        "target": target,
        "success": success,
        "open_ports": open_ports
    }

