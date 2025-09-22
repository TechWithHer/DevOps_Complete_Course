from flask import Flask, render_template, request
from NetToolbox.cloud.cicdtest import test_cicd
from NetToolbox.cloud.kubernetestest import test_kubernetes
from NetToolbox.cloud.s3test import test_s3
from NetToolbox.connectivity.pingtest import test_ping
from NetToolbox.connectivity.tcpudppingtest import test_tcp_udp_ping
from NetToolbox.connectivity.traceroutetest import test_traceroute
from NetToolbox.dns.cnametest import test_cname
from NetToolbox.dns.dnslookuptest import test_dns_lookup
from NetToolbox.dns.mmxtest import test_mx
from NetToolbox.security.firewalltest import test_firewall
from NetToolbox.security.portscantest import test_port_scan
from NetToolbox.security.weakcyphertest import test_weak_cipher
from NetToolbox.webservices.apitest import test_api
from NetToolbox.webservices.httptest import test_http
from NetToolbox.webservices.ssltest import test_ssl

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
