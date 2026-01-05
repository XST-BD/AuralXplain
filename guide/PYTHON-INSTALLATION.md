# Python Installation Guide

This guide will help you install Python on your system. Python is a versatile programming language required for running
this project. Follow the instructions below based on your operating system.

## Windows

1. Go to this link: https://www.python.org/downloads/windows/
2. Download the `Windows installer (64-bit)` or `Windows installer (32-bit)` from the Stable Releases section according
   to your Windows version.
3. Run the installer. Make sure to check the box that says `Add Python to PATH` before clicking "Install Now".
4. Follow the prompts to complete the installation.
5. After the installation is complete, verify it by opening Command Prompt and running:
   ```bash
   python --version
   ```

## macOS

1. Open Terminal.
2. Install Homebrew (if you haven't already) by running:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Once Homebrew is installed, run the following command to install Python:
   ```bash
   brew install python
   ```
4. After the installation is complete, verify it by running:
   ```bash
   python3 --version
   ```

## Linux

### Ubuntu / Debian

1. Open Terminal.
2. Update the package list:
   ```bash
   sudo apt install python3 python3-pip python3-venv -y
   ```
3. Install Python by running:
   ```bash
   sudo apt install python3
   ```
4. After the installation is complete, verify it by running:
   ```bash
   python3 --version
   ```

### Fedora

1. Open Terminal.
2. Install Python by running:
   ```bash
   sudo dnf install python3 python3-pip -y
   ```
3. After the installation is complete, verify it by running:
   ```bash
   python3 --version
   ```

### Arch / Manjaro

1. Open Terminal.
2. Install Python by running:
   ```bash
   sudo pacman -S python python-pip
   ```
3. After the installation is complete, verify it by running:
   ```bash
   python --version
   ```