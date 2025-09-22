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
