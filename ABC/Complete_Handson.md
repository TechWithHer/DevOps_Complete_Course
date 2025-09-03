Networking Hands-On Roadmap for DevOps

Phase 1: Basic Connectivity Checks (Foundation)
Goal: Understand connectivity between servers, ports, and external endpoints.

Tasks:
Launch two EC2 instances in the same region.
Use ping to test connectivity:
Public IP → EC21 → EC22 (test both directions).

Use traceroute or mtr to visualize the route between instances and to external sites.

Use nc (netcat) to check if specific ports (22, 80, 443, 3306) are open between instances.

Use curl / wget to access an HTTP endpoint from EC2.

Optional Automation:

Script to ping multiple endpoints and log results.

Phase 2: DNS & Name Resolution

Goal: Understand how DNS works internally and externally.

Tasks:

Use dig / nslookup to query:

Public domain (example.com)

Internal EC2 hostname (if using Route53 private hosted zone)

Compare DNS resolution inside VPC vs. public internet.

Edit /etc/resolv.conf and test custom DNS resolution.

Phase 3: IP, Ports & Interfaces

Goal: Get comfortable with instance-level networking.

Tasks:

View assigned IP addresses using ip addr or ifconfig.

Check open/listening ports with ss -tulnp or netstat -tulnp.

Inspect routing table with ip route.

Add a custom route to another subnet and test connectivity.

Optional Automation:

Script to check open ports and services, log results, alert if missing.

Phase 4: Security Groups & Firewalls

Goal: Learn traffic filtering and access control.

Tasks:

Modify Security Groups to allow/block:

SSH only from your IP

HTTP/HTTPS only from specific IPs

Test with curl or nc from EC2.

Explore NACLs for subnet-level control.

Optional Automation:

Script to audit SGs and NACLs for specific rules.

Phase 5: VPC Networking (AWS-Specific)

Goal: Build understanding of subnets, NAT, and routing.

Tasks:

Create a VPC with:

Public subnet → EC2 with public IP

Private subnet → EC2 without public IP

Attach an Internet Gateway to the VPC.

Configure route tables for public and private subnets.

Deploy NAT Gateway for private subnet outbound internet access.

Test connectivity:

Public EC2 → internet

Private EC2 → internet via NAT

Optional: Create VPC peering and test cross-VPC connectivity.

Phase 6: Load Balancers & Service Exposure

Goal: Understand how to expose services securely and distribute traffic.

Tasks:

Deploy a small web app on two EC2 instances.

Create an ALB (Application Load Balancer):

Configure target groups, listeners, and health checks

Verify traffic routing and failover:

Stop one EC2 → check ALB reroutes traffic

Test security with SGs on ALB and EC2s.

Phase 7: Bastion Host & VPN

Goal: Secure access to private instances.

Tasks:

Deploy a Bastion Host in the public subnet.

Connect to EC2 in private subnet via SSH agent forwarding.

Optional: Set up a simple VPN connection between your local machine and VPC.

Phase 8: Monitoring & Troubleshooting

Goal: Learn to detect and debug network issues.

Tasks:

Enable VPC Flow Logs and review inbound/outbound traffic.

Use tcpdump on EC2 to capture packets for HTTP/SSH traffic.

Use iftop / nload to monitor real-time bandwidth.

Optional: Send alerts if unexpected traffic is detected.

Phase 9: Service Discovery & Internal Networking

Goal: Understand internal service communication.

Tasks:

Deploy Docker Compose with two services (web + DB).

Verify connectivity via Docker network.

Test internal DNS-based service discovery.

Phase 10: Automation & Scripting

Goal: Integrate networking checks into daily DevOps workflow.

Tasks:

Create a shell script or Python script to:

Check connectivity to multiple endpoints

Check port availability

Log failures and send alerts (email/Telegram)

Optional: Integrate script with cron for scheduled execution.

✅ Outcome if completed:

You’ll have hands-on experience with all networking tasks a DevOps engineer faces.

You’ll also have scripts and automation checks ready for practical use.

This covers VPC, EC2, DNS, routing, load balancers, security, monitoring, and internal service communication.
