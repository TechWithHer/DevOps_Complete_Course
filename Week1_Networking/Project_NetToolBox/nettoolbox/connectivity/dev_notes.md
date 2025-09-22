DevOps can quickly debug network reachability and latency issues.
# Connectivity Tests (NetToolbox)

This folder contains basic connectivity test scripts:

- **pingtest.py** → ICMP ping check to a host.
- **tcpudppingtest.py** → TCP connection test and UDP packet send test.
- **traceroutetest.py** → Runs a traceroute to a host (limited hops for quick test).

### Requirements
- Linux/macOS for `ping` and `traceroute` (Windows may need `tracert`).
- Python 3.8+ (no extra libraries needed).
