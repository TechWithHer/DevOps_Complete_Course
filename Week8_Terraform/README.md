🔹 EC2 Instance Networking

ping → check connectivity between instances or to the internet.

curl / wget → test HTTP(S) endpoints from EC2.

traceroute / mtr → see path from EC2 to destination (helps with route table issues).

nc (netcat) → test if specific ports are reachable (e.g., DB port, app port).

ss / netstat → list active connections, listening ports.

ip addr / ip route → check private/public IPs and routing within the instance.

arp / ip neigh → local neighbor resolution (rare but can help for ENI debugging).

🔹 VPC / Networking Debugging

AWS CLI commands:

aws ec2 describe-vpcs → list VPCs

aws ec2 describe-subnets → list subnets & CIDRs

aws ec2 describe-route-tables → check routing rules

aws ec2 describe-security-groups → view security group rules

aws ec2 describe-network-interfaces → ENI details, private IPs, MACs

aws ec2 describe-instances → verify IP assignment and network status

VPC Flow Logs → check allowed/blocked traffic inside your VPC.

🔹 DNS & Endpoint Testing

dig / nslookup → test Route53 records.

curl -v → test connectivity to API Gateway, ELB, or other endpoints.

ping → test connectivity (if ICMP allowed by SG/NACL).

🔹 Security & Firewall

iptables -L → instance-level firewall rules (rare in AWS, usually SG/NACL handles it).

nmap → scan instance ports to verify open/closed ports (if allowed by SG).

🔹 Load Balancers & Public Services

curl / wget → test ELB endpoints.

dig → verify DNS for ALB/CNAME records.

🔹 Cloud-Native Debugging Tools

aws cloudwatch get-metric-data → monitor network traffic metrics.

aws logs tail <log-group> → check VPC flow logs or app logs in real-time.

aws ec2 get-console-output → for boot/network errors on instance launch.
