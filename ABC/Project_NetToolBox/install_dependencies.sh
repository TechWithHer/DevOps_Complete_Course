#!/bin/bash

echo "🔧 Installing required tools for NetToolbox..."

sudo apt update

# Basic Connectivity
sudo apt install -y iputils-ping traceroute mtr netcat telnet

# DNS & Domain Tools
sudo apt install -y dnsutils whois bind9-host

# Interface & Network Tools
sudo apt install -y net-tools iproute2 wireless-tools ethtool ifplugd

# Ports & Firewall Tools
sudo apt install -y nmap iptables net-tools iproute2

# Utilities
sudo apt install -y curl wget jq watch

# Optional (not used yet but might be)
sudo apt install -y speedtest-cli tcpdump

echo "✅ All tools installed!"
