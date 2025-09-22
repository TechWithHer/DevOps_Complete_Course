from flask import Flask, render_template, request
from nettoolbox.cloud_devops.cicd_test import test_cicd
from nettoolbox.cloud_devops.kubernetes_test import test_kubernetes
from nettoolbox.cloud_devops.s3_test import test_s3
from nettoolbox.connectivity.ping_test import test_ping
from nettoolbox.connectivity.tcp_udp_ping_test import tcp_udp_ping_test
from nettoolbox.connectivity.traceroute_test import test_traceroute
from nettoolbox.dns.cname_test import test_cname
from nettoolbox.dns.dns_lookup_test import test_dns_lookup
from nettoolbox.dns.mx_test import test_mx
from nettoolbox.security.firewall_test import test_firewall
from nettoolbox.security.port_scan_test import test_port_scan
from nettoolbox.security.weak_cipher_test import test_weak_cipher
from nettoolbox.web_services.api_test import test_api
from nettoolbox.web_services.http_test import test_http
from nettoolbox.web_services.ssl_test import test_ssl

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    status = None
    if request.method == "POST":
        category = request.form.get("category")
        target = request.form.get("target")

        if category == "cicd":
            result = test_cicd(target)
        elif category == "k8s":
            result = test_kubernetes(target)
        elif category == "s3":
            result = test_s3(target)
        elif category == "ping":
            result = test_ping(target)
        elif category == "tcp_udp":
            result = test_tcp_udp_ping(target)
        elif category == "traceroute":
            result = test_traceroute(target)
        elif category == "cname":
            result = test_cname(target)
        elif category == "dns":
            result = test_dns_lookup(target)
        elif category == "mx":
            result = test_mx(target)
        elif category == "firewall":
            result = test_firewall(target)
        elif category == "port_scan":
            result = test_port_scan(target)
        elif category == "weak_cipher":
            result = test_weak_cipher(target)
        elif category == "api":
            result = test_api(target)
        elif category == "http":
            result = test_http(target)
        elif category == "ssl":
            result = test_ssl(target)

        # Assume each test returns a string like "PASS: ..." or "FAIL: ..."
        if result.startswith("PASS"):
            status = "good"
        else:
            status = "bad"

    return render_template("index.html", result=result, status=status)
