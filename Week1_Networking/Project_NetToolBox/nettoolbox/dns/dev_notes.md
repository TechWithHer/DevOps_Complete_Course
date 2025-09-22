Verify DNS setup, email servers, domain validation (important for CI/CD & cloud infra).
# DNS Tests (NetToolbox)

This folder contains DNS-related test scripts:

- **cnametest.py** → Resolves CNAME records for a given domain.
- **dnslookuptest.py** → Resolves a domain name to its IP address.
- **mxtest.py** → Resolves MX (Mail Exchange) records for a domain.

### Requirements
- Python 3.8+
- `dnspython` library → install with `pip install dnspython`
