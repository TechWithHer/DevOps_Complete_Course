from flask import Flask, render_template, request
from nettoolbox.cloud_devops import cicd_test, kubernetes_test, s3_test
from nettoolbox.connectivity import ping_test, tcp_udp_ping_test, traceroute_test
from nettoolbox.dns import cname_test, dns_lookup_test, mx_test
from nettoolbox.security import firewall_test, port_scan_test, weak_cipher_test
from nettoolbox.web_services import api_test, http_test, ssl_test

# ✅ Define Flask app before using it
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tests = {}  # initialize as empty dict
    if request.method == "POST":
        category = request.form.get("category")
        target = request.form.get("target")

        if category == "cloud":
            tests = {
                "cicd": ("CI/CD Test", cicd_test.test_cicd(target)),
                "k8s": ("Kubernetes Test", kubernetes_test.test_kubernetes(target)),
                "s3": ("S3 Test", s3_test.test_s3(target)),
            }
        elif category == "connectivity":
            tests = {
                "ping": ("Ping Test", ping_test.test_ping(target)),
                "tcp_udp": ("TCP/UDP Test", tcp_udp_ping_test.test_tcp_udp_ping(target)),
                "traceroute": ("Traceroute", traceroute_test.test_traceroute(target)),
            }
        elif category == "dns":
            tests = {
                "cname": ("CNAME Test", cname_test.test_cname(target)),
                "dns": ("DNS Lookup", dns_lookup_test.test_dns_lookup(target)),
                "mx": ("MX Test", mx_test.test_mx(target)),
            }
        elif category == "security":
            tests = {
                "firewall": ("Firewall Test", firewall_test.test_firewall(target)),
                "port_scan": ("Port Scan", port_scan_test.test_port_scan(target)),
                "weak_cipher": ("Weak Cipher Test", weak_cipher_test.test_weak_cipher(target)),
            }
        elif category == "web":
            tests = {
                "api": ("API Test", api_test.test_api(target)),
                "http": ("HTTP Test", http_test.test_http(target)),
                "ssl": ("SSL Test", ssl_test.test_ssl(target)),
            }

    return render_template("index.html", tests=tests)

# ✅ Add this so Flask actually runs when you execute app.py
if __name__ == "__main__":
    # host="0.0.0.0" makes it accessible outside EC2 on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
