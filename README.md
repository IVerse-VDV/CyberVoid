# 🛡️ CyberTools Collection

<div align="center">

![Security Banner](assets/2092745.png)

### Your All-in-One Security Swiss Army Knife
*Powerful tools for the modern security professional*

[![GitHub stars](https://img.shields.io/github/stars/yourusername/cyber-tools?style=social)](https://github.com/yourusername/cyber-tools/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/yourusername/cyber-tools/pulls)

[Explore Documentation](#) | [Installation Guide](#) | [Contributing](https://github.com/IVerse-VDV/CyberVoid/pulls) | [Report Bug](https://github.com/IVerse-VDV/CyberVoid/issues)

</div>

##  Why Choose CyberTools?

> *"The first step in securing your system is having the right tools at your disposal."*

In a world where cyber threats evolve daily, staying ahead requires the right arsenal. CyberTools Collection brings you a carefully curated suite of security tools that combine power with simplicity. Whether you're a seasoned security professional or just starting your cybersecurity journey, our tools are designed to meet your needs.

##  Featured Tools



>  **Fun Fact**: A 12-character random password would take centuries to crack using current technology!

### 🌐 [IP-Check](https://github.com/rexzea/Net-Phantom)
A Python based IP address analysis tool that provides detailed information about IP addresses and domains. This tool fetches and analyzes various aspects of an IP address or domain, including geolocation, network information, DNS records, SSL certificates, WHOIS data, and port scanning.

## Features

#### Core Functionality
- IPv4 and IPv6 support
- Domain name resolution
- Response time measurement
- Detailed geolocation data
- Network information analysis

### Advanced Information Gathering
- **DNS Analysis**
  - Multiple record types (A, AAAA, MX, NS, TXT, SOA, CNAME)
  - Nameserver information
  - Reverse DNS lookup

- **Security Information**
  - SSL/TLS certificate details
  - Port scanning with service detection
  - Banner grabbing for open ports
  - Proxy/VPN detection

- **Domain Information**
  - WHOIS data retrieval
  - Registration details
  - Domain status
  - Registrar information

##### Data Management
- Organized data storage in `dataV/` directory
- Raw data storage in JSON format
- Interactive visualizations
- Historical data viewing
- Structured report generation

#### Requirements

- Python 3.7+
- Required packages:
  ```
  requests
  dnspython
  python-whois
  pyOpenSSL
  plotly
  pandas
  ```


#### Result
```bash

Basic Information:
IP Address: 8.8.8.8
Response Time: 0.373 detik
Tipe: Non-Mobile
Proxy/VPN: Tidak
Hosting/Datacenter: Ya

Location:
Continent: North America (NA)
Country: United States (US)
Region: Virginia (VA)
City: Ashburn
District:
Zip Code: 20149
Coordinate: 39.03, -77.5

Network Network:
ISP: Google LLC
Organization: Google Public DNS
AS Number: AS15169 Google LLC
AS Name: GOOGLE
Reverse DNS: dns.google

DNS Information:
Record DNS:
- A: 8.8.4.4, 8.8.8.8
- AAAA: 2001:4860:4860::8888, 2001:4860:4860::8844
- NS: ns4.zdns.google., ns3.zdns.google., ns2.zdns.google., ns1.zdns.google.
- TXT: "v=spf1 -all", "https://xkcd.com/1361/"
- SOA: ns1.zdns.google. cloud-dns-hostmaster.google.com. 1 21600 3600 259200 300
Nameservers: ns3.zdns.google., ns2.zdns.google., ns1.zdns.google., ns4.zdns.google.

SSL Information:
Issuer: [(b'C', b'US'), (b'O', b'Google Trust Services'), (b'CN', b'WR2')]
Subject: [(b'CN', b'dns.google')]
Valid From: b'20250106083801Z'
Valid Until: b'20250331083800Z'
Version: 2

WHOIS Information:
Registrar: MarkMonitor Inc.
Created: 2018-04-16 22:57:01
Expires: 2025-04-16 22:57:01
Updated: 2024-03-20 10:02:54
Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited, clientTransferProhibited https://icann.org/epp#clientTransferProhibited, clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
Nameservers: ns1.zdns.google, ns2.zdns.google, ns3.zdns.google, ns4.zdns.google
```


#### Directory Structure

```
dataV/
├── raw/           # Raw JSON data
├── reports/       # Formatted reports
├── visualizations/# Interactive visualizations
└── history/       # Search history
```

#### Output Information

The tool provides information including:
- Basic IP information
- Geographical data
- Network details
- DNS records
- SSL certificate information
- WHOIS data
- Port scan results
- Response times

  
> 🎯 **Use Case**: Perfect for threat intelligence and network security assessments!

### 📊 [Local Device Monitor](https://github.com/rexzea/Simple-Monitoring)
## Project Summary
This Network Monitoring System is a Python-based tool designed to provide monitoring of network infrastructure, device health, and WiFi connectivity. By utilizing these monitoring techniques, it offers real-time analysis and reporting of network-related metrics.

#### Main Features

##### System Monitoring
- System resource tracking (CPU, Memory, Disk)
- Platform-specific system information retrieval
- Performance logging and analysis

##### Network Intelligence
- Network interface scanning
- IP address and hostname resolution
- Connection status and network topology mapping
- WiFi network detection and analysis

##### Security & Logging
- Robust logging mechanism
- Security-based network scanning
- Concurrent processing for efficient monitoring
- SQLite database integration for persistent data storage

#### Technologies Used
- **Language**: Python 3.8+
- **Main Libraries**:
  - `psutil`: System and process utilities
  - `platform`: System information retrieval
  - `socket`: Network communication
  - `threading`: Concurrent operations
  - `sqlite3`: Database management
  - `requests`: HTTP networking

   **MUST BE INSTALLED!**

#### Prerequisites
- Python 3.8 or higher
- Required Python libraries (see `External Tools`)
- Administrative/root access recommended

#### Installation Clone
check the repository [in here](https://github.com/rexzea/Simple-Monitoring)
```bash
https://github.com/rexzea/Simple-Monitoring.git
```

#### External Tools
```python
import psutil
import platform
import socket
import time
import logging
import datetime
import socket
import json
import threading
import time
import sqlite3
import re
import os
import subprocess
import concurrent.futures
import uuid
import requests
import ipaddress
```

#### Preview
```bash
--- Network Monitoring ---
Network: {'ssid': 'Not shown', 'platform': 'Windows'}
Connected Devices: 0
Download Speed: 18.81 Mbps
Upload Speed: 9.4 Mbps
Signal Strength: 84%
Local IP: not shown
Subnet: not shown
Device List: not shown
Monitoring stopped.
```

> 🚀 **Performance Tip**: Set up custom alerts to catch resource hogs before they impact your system!

### 🎭 [MAC Address Changer](#)
Master of disguise for your network identity! Change your MAC address with confidence:
- One click randomization
- Vendor specific MACs
- Automatic backup
- Cross platform support
- Safety checks built-in

> ⚡ **Quick Tip**: Always backup your original MAC address before making changes!

### 📱 [OSINT Phone Number](https://github.com/rexzea/PhoneDetective)
Turn any phone number into a goldmine of intelligence:
- Global number validation
- Social media footprint
- Carrier identification
- Risk assessment
- Historical data analysis

> 🔍 **Investigation Tip**: Cross reference findings with social media for better results!

### 🕸️ [OSINT Web](https://github.com/rexzea/Magic-Eye-Osint-Tools)
Your digital microscope for web reconnaissance:
- Deep domain analysis
- Technology stack detection
- Security assessment
- Historical records
- Comprehensive reporting

> 🎯 **Best Practice**: Always verify findings through multiple sources!

### 🔒 [Password Checker](https://github.com/rexzea/Simple-password-strength-checker)
Dont just guess - know how strong your passwords really are:
- Advanced strength analysis
- Pattern detection
- Breach database checking
- Policy compliance
- Real-time feedback

### 🔐 [AES Text Encryptor](https://github.com/rexzea/AES-Text-Encryptor) 
Transform your sensitive text into unbreakable code with military grade encryption. Our AES-256 implementation doesnt just encrypt - it fortifies your data with:
- Real-time encryption/decryption
- Multiple cipher modes (CBC, ECB, CTR)
- Intuitive key management
- File encryption support
- Cross platform compatibility

> 💡 **Tip**: Use CBC mode for enhanced security in most scenarios!

### 🎲 [Secure Password Generator](https://github.com/rexzea/SecurePass-Generator)
Stop using "password123"! Create fortress strong passwords that even supercomputers cant crack. Features include:
- Quantum resistant random generation
- Customizable complexity rules
- Built-in password manager
- Password strength analytics
- Secure storage with AES-256

> 💪 **Strength Tip**: Mix characters, numbers, and symbols for maximum security!

### 🦠 [Python Virus Sample](#)
Educational malware analysis in a safe environment:
- Controlled environment
- Detailed documentation
- Learning resources
- Safety mechanisms
- Analysis tools

> ⚠️ **Safety First**: Always use in an isolated environment!

### 🔍 [URL Scanner](https://github.com/rexzea/Simple-URl-Checker)
Your first line of defense against malicious websites:
- Malware detection
- SSL verification
- Vulnerability scanning
- Content analysis
- Detailed reports

> 🛡️ **Security Tip**: Scan unknown URLs before clicking!

## 🚀 Quick Start

Get up and running in minutes:

```bash
# Clone with style
git clone https://github.com/IVerse-VDV/CyberVoid.git

# Enter the matrix
cd cyber-tools

# Power up
pip install -r requirements.txt

# Launch your first tool
python cyber-tools/ip-check/main/react-ip-checker.py
```

## 🎨 Features That Make Us Special

- 🔥 **Modern Interface**: Clean, intuitive, and powerful
- 🚀 **Lightning Fast**: Optimized for performance
- 🛡️ **Security First**: Built with security best practices
- 📱 **Cross-Platform**: Works on Windows, Linux, and MacOS
- 🔧 **Extensible**: Easy to modify and enhance
- 📚 **Well Documented**: Clear, comprehensive documentation

## 🤝 Join Community

Your contributions make CyberTools better! Whether you're:
- 🐛 Hunting bugs
- ✨ Adding features
- 📝 Improving documentation
- 🎨 Enhancing UI/UX

We welcome your pull requests!

## 📞 Connect With Us

<div align="center">

[![Twitter Follow](https://img.shields.io/twitter/follow/UniVoid?style=social)](https://twitter.com/UniVoid)
[![Discord](https://img.shields.io/discord/YOUR_DISCORD_ID?style=social&logo=discord)](https://discord.gg/UniVoid)
[![Reddit User Karma](https://img.shields.io/reddit/user-karma/combined/UniVoid?style=social)](https://reddit.com/u/UniVoid)

</div>

Got questions? We've got answers:
- 📧 Email: -
- 💬 Discord: [UniVoid](#)
- 🐦 Twitter: [UniVoid](#)
- 🌟 GitHub: [Issue](#)

## 📜 License

Released under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### Ready to level up your security game? 
⭐ Star us on GitHub and join our community!

[Get Started](#) | [View Demo](#) | [Report Bug](https://github.com/IVerse-VDV/CyberVoid/issues) | [Request Feature](https://github.com/IVerse-VDV/CyberVoid/pulls)

</div>
