#!/bin/bash
# NetToolBox - Install Dependencies Script
# This script installs system and Python dependencies for the project.
# Safe to run multiple times (idempotent).

set -e  # Exit immediately if a command fails

echo "🔹 Updating system packages..."
if command -v apt-get &> /dev/null; then
    sudo apt-get update -y
elif command -v yum &> /dev/null; then
    sudo yum update -y
else
    echo "❌ Neither apt-get nor yum found. Please install dependencies manually."
    exit 1
fi

echo "🔹 Checking for Python3..."
if ! command -v python3 &> /dev/null; then
    echo "Installing Python3..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get install -y python3 python3-pip
    elif command -v yum &> /dev/null; then
        sudo yum install -y python3 python3-pip
    fi
else
    echo "✅ Python3 is already installed."
fi

echo "🔹 Installing required Python packages from requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip3 install --requirement requirements.txt --upgrade-strategy only-if-needed
    echo "✅ Python dependencies installed."
else
    echo "⚠️ requirements.txt not found. Skipping Python dependencies."
fi

echo "🎉 Setup complete. You’re ready to run NetToolBox!"

