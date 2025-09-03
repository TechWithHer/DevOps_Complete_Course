# 🛠️ Project_NetToolBox

A **Network Troubleshooting & DevOps Toolkit** built in Python, designed to provide practical, hands-on utilities for diagnosing and resolving network issues.  
This project is also a learning journey into the **OSI & TCP/IP models**, bridging theoretical knowledge with real-world troubleshooting.

---

## 📌 Features

- **Layered Approach** – Tools mapped to OSI & TCP/IP layers for structured learning  
- **Essential DevOps CLI Wrappers** – ping, traceroute, netstat, curl, and more  
- **Connectivity Checks** – Host reachability, DNS resolution, and port scanning  
- **Interactive CLI** – Simple menu-driven interface for quick use  
- **Extendable** – Easy to add new troubleshooting modules  

---

## 📚 Learning Objectives

- Gain a **practical understanding** of OSI & TCP/IP layers  
- Use Python to replicate and extend standard networking commands  
- Build a **real-world DevOps utility** while learning networking fundamentals  
- Practice **systematic troubleshooting** for everyday issues  

---

## 🏗️ Project Structure

Project_NetToolBox/
│── nettoolbox.py # Main CLI script
│── modules/ # Individual feature modules
│ ├── layer1_physical.py
│ ├── layer2_datalink.py
│ ├── layer3_network.py
│ ├── layer4_transport.py
│ └── layer7_application.py
│── utils/ # Helper functions
│── README.md # Documentation


---

## ⚙️ Installation

1. Clone the repository  
   `git clone https://github.com/your-username/Project_NetToolBox.git`

2. Navigate to project directory  
   `cd Project_NetToolBox`

3. (Optional) Create virtual environment  
   - Linux/Mac: `python3 -m venv venv && source venv/bin/activate`  
   - Windows: `python -m venv venv && venv\Scripts\activate`

4. Install dependencies  
   `pip install -r requirements.txt`

---

## 🚀 Usage

Run the toolkit with:

`python nettoolbox.py`

You’ll see an **interactive menu** to choose from different troubleshooting tools.

---

## 🧩 Example Tools

- **Physical/Data Link Layer**: Interface status, MAC address lookup  
- **Network Layer**: Ping, traceroute, DNS resolution  
- **Transport Layer**: Port scanning, socket tests  
- **Application Layer**: HTTP requests, API checks  

---

## 📈 Roadmap

- [ ] Add logging and reporting features  
- [ ] Expand into **security auditing** modules  
- [ ] Host on **AWS EC2** for real-world use  
- [ ] Build a simple **web dashboard** interface  

---

## 🤝 Contributing

Contributions, ideas, and suggestions are welcome!  
Fork the repo and submit a PR, or open an issue for discussion.

---

## 📜 License

This project is licensed under the MIT License – feel free to use and adapt.

---

## 👩‍💻 Author

**Ayushi Singh**  
Tech Content Creator | DevOps Enthusiast | Founder @ Strenure
