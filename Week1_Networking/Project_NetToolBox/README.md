NetToolbox 🛠️

A lightweight Python toolkit for network troubleshooting and learning.

📌 Overview

NetToolbox is a command-line toolkit built in Python to help troubleshoot and understand networks.
It is designed for learners, DevOps engineers, and system admins who want to quickly test connectivity, resolve network issues, and explore how different protocols work — all from a single interactive tool.

✨ Features

🔍 Ping Test – Verify connectivity to a host.

🌐 DNS Lookup – Resolve domain names to IP addresses.

📡 Port Scanner – Check open ports on a host.

🛰️ IP Info – Get your public IP and local network info.

📜 Traceroute (optional) – Trace the route packets take (can be extended).

📖 Educational Mode – Understand how these commands map to OSI/TCP layers.

🛠️ Installation
1. Clone the repository
git clone https://github.com/your-username/NetToolbox.git
cd NetToolbox

2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

🚀 Usage

Run the tool with:

python main.py


You’ll see an interactive menu like:

1. Ping a host
2. DNS lookup
3. Port scan
4. Get IP info
5. Exit


Example:

Enter choice: 1
Enter host: google.com
Pinging google.com...
Reply from 142.250.72.14: time=20ms

📂 Project Structure
NetToolbox/
│── nettoolbox/        # Core Python package
│   ├── ping.py        # Ping functionality
│   ├── dns_lookup.py  # DNS resolution
│   ├── port_scan.py   # Port scanner
│   ├── ip_info.py     # Get IP info
│   └── __init__.py
│
│── main.py            # Entry point script
│── requirements.txt   # Dependencies
│── README.md          # Documentation

🧭 Roadmap

 Add traceroute functionality

 Add monitoring alerts (email/Telegram)

 Build simple web dashboard for results

 Package as a PyPI module

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open an issue
 or submit a PR.

📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.
