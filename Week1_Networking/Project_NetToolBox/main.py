import sys
from nettoolbox.cloud_devops import cicd_test, kubernetes_test, s3_test
from nettoolbox.connectivity import ping_test, tcp_udp_ping_test, traceroute_test
from nettoolbox.dns import cname_test, dns_lookup_test, mx_test
from nettoolbox.security import firewall_test, port_scan_test, weak_cipher_test
from nettoolbox.web_services import api_test, http_test, ssl_test

def main():
    print("=== NetToolBox CLI ===")
    print("Choose a test category:")
    print("1. Cloud & DevOps")
    print("2. Connectivity")
    print("3. DNS")
    print("4. Security")
    print("5. Web Services")
    choice = input("Enter choice: ")

    if choice == "1":
        service = input("Enter service name (domain/bucket/cluster): ")
        print(cicd_test.test_cicd(service))
        print(kubernetes_test.test_kubernetes(service))
        print(s3_test.test_s3(service))

    elif choice == "2":
        target = input("Enter host/IP: ")
        print(ping_test.test_ping(target))
        print(tcp_udp_ping_test.test_tcp_udp_ping(target))
        print(traceroute_test.test_traceroute(target))

    elif choice == "3":
        domain = input("Enter domain: ")
        print(cname_test.test_cname(domain))
        print(dns_lookup_test.test_dns_lookup(domain))
        print(mx_test.test_mx(domain))

    elif choice == "4":
        host = input("Enter host/IP: ")
        print(firewall_test.test_firewall(host))
        print(port_scan_test.test_port_scan(host))
        print(weak_cipher_test.test_weak_cipher(host))

    elif choice == "5":
        url = input("Enter full URL (https://...): ")
        print(api_test.test_api(url))
        print(http_test.test_http(url))
        print(ssl_test.test_ssl(url))

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
