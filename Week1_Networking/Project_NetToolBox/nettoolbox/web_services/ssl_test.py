# nettoolbox/web_services/ssl_test.py
import ssl
import socket
import time
from datetime import datetime
from urllib.parse import urlparse

def test_ssl(url: str, timeout: float = 4.0) -> dict:
    """
    Get SSL certificate info from host:port (default 443).
    Accepts full URL or host.
    """
    start = time.time()
    host = url
    port = 443
    try:
        parsed = urlparse(url)
        if parsed.scheme:
            host = parsed.hostname or host
            if parsed.port:
                port = parsed.port
    except Exception:
        pass

    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
        return {
            "test": "web_services.ssl",
            "target": f"{host}:{port}",
            "success": True,
            "output": {"cert_subject": cert.get("subject"), "issuer": cert.get("issuer"), "notBefore": cert.get("notBefore"), "notAfter": cert.get("notAfter"), "cipher": cipher},
            "error": None,
            "duration": time.time() - start,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
    except Exception as e:
        return {
            "test": "web_services.ssl",
            "target": f"{host}:{port}",
            "success": False,
            "output": None,
            "error": str(e),
            "duration": time.time() - start,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
