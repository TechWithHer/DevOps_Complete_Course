# NetToolBox/ssl_check.py
import ssl
import socket
from datetime import datetime

def run(target, port=443):
    """
    Checks the SSL/TLS certificate of the target.
    Returns issuer, expiry date, and validity status.
    """
    context = ssl.create_default_context()
    try:
        with socket.create_connection((target, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=target) as ssock:
                cert = ssock.getpeercert()

                issuer = dict(x[0] for x in cert['issuer'])
                issuer_str = issuer.get('organizationName', str(issuer))

                not_after = cert['notAfter']
                expiry_date = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")

                valid = expiry_date > datetime.utcnow()

                return {
                    "test": "SSL/TLS Check",
                    "target": target,
                    "success": valid,
                    "issuer": issuer_str,
                    "expiry_date": expiry_date.strftime("%Y-%m-%d %H:%M:%S"),
                }
    except Exception as e:
        return {
            "test": "SSL/TLS Check",
            "target": target,
            "success": False,
            "error": str(e)
        }

