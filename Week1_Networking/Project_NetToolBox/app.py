from flask import Flask, render_template, request
from nettoolbox.cloud_devops import cicd_test, kubernetes_test, s3_test
from nettoolbox.connectivity import ping_test, tcp_udp_ping_test, traceroute_test
from nettoolbox.dns import cname_test, dns_lookup_test, mx_test
from nettoolbox.security import firewall_test, port_scan_test, weak_cipher_test
from nettoolbox.web_services import api_test, http_test, ssl_test

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tests = None
    if request.method == "POST":
        category = request.form.get("category")
        target = request.form.get("target")

        if category == "cloud":
            tests = [
                cicd_test.test_cicd(target),
                kubernetes_test.test_kubernetes(target),
                s3_test.test_s3(target),
            ]
        elif category == "connectivity":
            tests = [
                ping_test.test_ping(target),
                tcp_udp_ping_test.test_tcp_ping(target),
                traceroute_test.test_traceroute(target),
            ]
        elif category == "dns":
            tests = [
                cname_test.test_cname(target),
                dns_lookup_test.test_dns_lookup(target),
                mx_test.test_mx(target),
            ]
        elif category == "security":
            tests = [
                firewall_test.test_firewall(target),
                port_scan_test.test_port_scan(target),
                weak_cipher_test.test_weak_cipher(target),
            ]
        elif category == "web":
            tests = [
                api_test.test_api(target),
                http_test.test_http(target),
                ssl_test.test_ssl(target),
            ]

    return render_template("index.html", tests=tests)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
