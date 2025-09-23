from flask import Flask, render_template, request
from nettoolbox.cloud_devops.cicd_test import test_cicd
from nettoolbox.cloud_devops.kubernetes_test import test_kubernetes
from nettoolbox.cloud_devops.s3_test import test_s3
from nettoolbox.connectivity.ping_test import test_ping
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
    message = None

    if request.method == "POST":
        category = request.form.get("category")
        target = request.form.get("target")

        # Map category to corresponding test function
        test_functions = {
            "cicd": test_cicd,
            "k8s": test_kubernetes,
            "s3": test_s3,
            "ping": test_ping,
            "traceroute": test_traceroute,
            "cname": test_cname,
            "dns": test_dns_lookup,
            "mx": test_mx,
            "firewall": test_firewall,
            "port_scan": test_port_scan,
            "weak_cipher": test_weak_cipher,
            "api": test_api,
            "http": test_http,
            "ssl": test_ssl,
        }

        test_func = test_functions.get(category)
        if test_func:
            result = test_func(target)

            # Determine status based on 'success' key if present
            if isinstance(result, dict):
                success = result.get("success", False)
                status = "good" if success else "bad"

                # Create a user-friendly message
                if success:
                    message = f"PASS: {result.get('target', 'Target')} test succeeded."
                else:
                    error = result.get("error", "Unknown error")
                    message = f"FAIL: {result.get('target', 'Target')} test failed. Error: {error}"
            else:
                # fallback if test_func returns a string
                status = "good" if str(result).startswith("PASS") else "bad"
                message = str(result)

    return render_template("index.html", result=result, status=status, message=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
