# 🛠️ NetToolbox

NetToolbox is a **network and cloud testing toolkit** built with Python.
It provides both a **Command-Line Interface (CLI)** and a **Web Dashboard** to perform essential DevOps, networking, DNS, security, and web service checks.

Designed with **professional UI** (dark metallic + neon theme ✨), it helps engineers test infrastructure quickly and visually.

---

## 📂 Project Structure

```
NetToolbox/
├── app.py                 # Web interface (Flask app)
├── main.py                # CLI interface
├── requirements.txt       # Dependencies (reference only)
├── templates/
│   └── index.html         # Web dashboard
├── static/
│   └── style.css          # Styling for the dashboard
├── nettoolbox/            # Core package
│   ├── cloud_devops/
│   │   ├── cicd_test.py
│   │   ├── kubernetes_test.py
│   │   └── s3_test.py
│   ├── connectivity/
│   │   ├── ping_test.py
│   │   └── traceroute_test.py
│   ├── dns/
│   │   ├── cname_test.py
│   │   ├── dns_lookup_test.py
│   │   └── mx_test.py
│   ├── security/
│   │   ├── firewall_test.py
│   │   ├── port_scan_test.py
│   │   └── weak_cipher_test.py
│   └── web_services/
│       ├── api_test.py
│       ├── http_test.py
│       └── ssl_test.py
```

---

## 🚀 Features

* **Cloud/DevOps Tests**

  * CI/CD connectivity check
  * Kubernetes test
  * AWS S3 test

* **Connectivity Tests**

  * Ping test
  * Traceroute test

* **DNS Tests**

  * CNAME lookup
  * DNS record lookup
  * MX record check

* **Security Tests**

  * Firewall reachability
  * Port scan
  * Weak cipher check

* **Web Services Tests**

  * API test
  * HTTP response check
  * SSL certificate validation

---

## ⚡ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TechWithHer/DevOps_Complete_Course/tree/main/Week1_Networking/Project_NetToolBox
   cd Project_NetToolBox
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥️ Usage

### 1. Run as Web App (Flask)

Start the Flask app:

```bash
python app.py
```

By default it runs at:

```
http://127.0.0.1:5000
```

If running on EC2, make it public:

```python
app.run(debug=True, host="0.0.0.0", port=5000)
```

#### 🌐 Web Dashboard

* Enter a **domain/IP** in the input field.
* Click on any **test button**.
* Results will show in **green** (PASS) or **red** (FAIL).

---

### 2. Run as CLI

Use `main.py` for terminal-based testing:

```bash
python main.py --category dns --test cname --target example.com
```

Example:

```bash
python main.py --category connectivity --test ping --target 8.8.8.8
```

---

## 📋 Requirements

Example `requirements.txt` (for reference only):

```
Flask
requests
dnspython
python-nmap
cryptography
```

---
## About Requirements

Flask → UI/web framework.
requests → HTTP checks.
dnspython → DNS checks.
python-nmap → Port scans.
cryptography → SSL/cipher strength analysis.

---

## 🎨 UI Preview

* **Dark metallic background** with **neon glow buttons**
* Results:

  * ✅ Green → PASS / secure / reachable
  * ❌ Red → FAIL / insecure / unreachable

---

## 🛡️ Security Note

This tool is for **educational and testing purposes only**.
Do not use it against systems you do not own or have permission to test.

---

## 🤝 Contributing

Pull requests are welcome! Please fork the repo and submit PRs with improvements.

---

## 📜 License

MIT License © 2025 Ayushi Singh

---
<img width="904" height="621" alt="Screenshot 2025-09-23 at 10 02 08 AM" src="https://github.com/user-attachments/assets/cfad5656-dbc6-4ecd-a6b9-931681afa3be" />
