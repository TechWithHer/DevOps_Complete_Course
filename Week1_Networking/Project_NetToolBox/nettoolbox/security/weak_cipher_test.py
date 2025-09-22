# nettoolbox/security/weak_cipher_test.py
import ssl
import socket
import time
from datetime import datetime

_WEAK_INDICATORS = ["RC4", "DES", "NULL", "EXPORT", "3DES"]

def test_weak_cipher(host: str, port: int = 443, timeout: float = 4.0) -> dict:
    """
    Attempts TLS handshake and returns negotiated cipher. Flags a warning if negotiated cipher name
    contains keywords in _WEAK_INDICATORS. This is a minimal check (not an exhaustive cipher scan).
    """
    start = time.time()
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cipher = ssock.cipher()
                cipher_name = cipher[0] if cipher else None
                weak = any(ind in (cipher_name or "").upper() for ind in _WEAK_INDICATORS)
                result = {
                    "test": "security.weak_cipher",
                    "target": f"{host}:{port}",
                    "success": True,
                    "output": {"negotiated_cipher": cipher_name, "weak": weak},
                    "error": None,
                    "duration": time.time() - start,
                    "timestamp": datetime.utcnow().isoformat() + "Z"
                }
                return result
    except Exception as e:
        return {
            "test": "security.weak_cipher",
            "target": f"{host}:{port}",
            "success": False,
            "output": None,
            "error": str(e),
            "duration": time.time() - start,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
