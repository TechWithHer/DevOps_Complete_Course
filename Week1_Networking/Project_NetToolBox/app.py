from flask import Flask, render_template, request, jsonify
from nettoolbox.cloud_devops import cicd_test, kubernetes_test, s3_test
from nettoolbox.connectivity import ping_test, tcp_udp_ping_test, traceroute_test
from nettoolbox.dns import cname_test, dns_lookup_test, mx_test
from nettoolbox.security import firewall_test, port_scan_test, weak_cipher_test
from nettoolbox.web_services import api_test, http_test, ssl_test

app = Flask(__name__)

# Mapping test names to functions
TEST_FUNCTIONS = {
    # Cloud & DevOps
    "cicd": cicd_test.test_cicd,
    "kubernetes": kubernetes_test.test_kubernetes,
    "s3": s3_test.test_s3,
    # Connectivity
    "ping": ping_test.test_ping,
    "tcp_udp_ping": tcp_udp_ping_test.test_tcp_udp_ping,
    "traceroute": traceroute_test.test_traceroute,
    # DNS
    "cname": cname_test.test_cname,
    "dns_lookup": dns_lookup_test.test_dns_lookup,
    "mx": mx_test.test_mx,
    # Security
    "firewall": firewall_test.test_firewall,
    "port_scan": port_scan_test.test_port_scan,
    "weak_cipher": weak_cipher_test.test_weak_cipher,
    # Web Services
    "api": api_test.test_api,
    "http": http_test.test_http,
    "ssl": ssl_test.test_ssl,
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_test", methods=["POST"])
def run_test():
    data = request.get_json()
    test_name = data.get("test")
    target = data.get("target")

    if not test_name or not target:
        return jsonify({"error": "Missing test or target"}), 400

    func = TEST_FUNCTIONS.get(test_name)
    if not func:
        return jsonify({"error": f"Unknown test: {test_name}"}), 400

    try:
        result = func(target)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
