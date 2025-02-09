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
#### About PhoneDetective
PhoneDetective is an OSINT (Open Source Intelligence) tool designed to uncover hidden information behind phone numbers effortlessly. With an intuitive interface, PhoneDetective helps you gather intelligence from various open sources.

#### Key Features

##### 🔹 Validation

- Automatic phone number format detection
- Real time validation to ensure accuracy
- National format (Indonesia)


##### 🔹 Analysis

- Identify mobile providers
- Detect geographical location
- Phone number registration history

  
##### 🔹 Reports

- Export results in JSON format
- Interactive data visualization
- Structured analysis summary

  
##### Getting Started

- Prerequisites
- Python 3.6+
- pip (Python package installer)
- Internet connection

#### Preview
```python
              
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Field                ┃ Value            ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Format Internasional │ +62 898-8610-455 │
│ Format Nasional      │ 0898-8610-455    │
│ Format E164          │ +628988610455    │
│ Kode Negara          │ +62              │       # My contact
│ Nomor Nasional       │ 8988610455       │
│ Tipe                 │ 1                │
│ Valid                │ True             │
│ Kemungkinan          │ True             │
└──────────────────────┴──────────────────┘
```

##### Output (JSON)

```json
{
  "number": "+62812XXXXX",
  "valid": true,
  "provider": "Telkomsel",
  "location": {
    "province": "DKI Jakarta",
    "region": "Indonesia"
  },
  "risk_score": 0.2,
  "last_seen": "2024-12-15"
}
```

> 🔍 **Investigation Tip**: Cross reference findings with social media for better results!

### 🕸️ [OSINT Web](https://github.com/rexzea/Magic-Eye-Osint-Tools)
#### Overview

Magic Eye is a powerful OSINT (Open Source Intelligence) tool designed for comprehensive website analysis and intelligence gathering. With four specialized modes of operation, it provides flexible and detailed insights into web infrastructure, content, and security aspects.

#### Features

-  Four specialized analysis modes
-  Multiple output formats (JSON/CSV)
-  Real time data processing
-  Deep website crawling capabilities
-  Security focused analysis options


#### Modes
##### 1. Regular Mode
> The versatile reconnaissance mode for quick analysis.

##### 2. Specific Mode
> Specialized analysis for ".com" domains with structured output.

##### 3. Hunter Mode
> Advanced link discovery and relationship mapping.

##### 4. Hazard Mode
> Technical security analysis and infrastructure mapping.



#### To know more details about all modes, [Click here](https://github.com/rexzea/Magic-Eye-Osint-Tools)

#### Usage

```bash
 ███▄ ▄███▓ ▄▄▄        ▄████  ██▓ ▄████▄     ▓█████▓██   ██▓▓█████ 
▓██▒▀█▀ ██▒▒████▄     ██▒ ▀█▒▓██▒▒██▀ ▀█     ▓█   ▀ ▒██  ██▒▓█   ▀ 
▓██    ▓██░▒██  ▀█▄  ▒██░▄▄▄░▒██▒▒▓█    ▄    ▒███    ▒██ ██░▒███   
▒██    ▒██ ░██▄▄▄▄██ ░▓█  ██▓░██░▒▓▓▄ ▄██▒   ▒▓█  ▄  ░ ▐██▓░▒▓█  ▄ 
▒██▒   ░██▒ ▓█   ▓██▒░▒▓███▀▒░██░▒ ▓███▀ ░   ░▒████▒ ░ ██▒▓░░▒████▒
░ ▒░   ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░▓  ░ ░▒ ▒  ░   ░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░
░  ░      ░  ▒   ▒▒ ░  ░   ░  ▒ ░  ░  ▒       ░ ░  ░▓██ ░▒░  ░ ░  ░
░      ░     ░   ▒   ░ ░   ░  ▒ ░░              ░   ▒ ▒ ░░     ░   
       ░         ░  ░      ░  ░  ░ ░            ░  ░░ ░        ░  ░
                                 ░                  ░ ░

cr : rexzea
==================================================
Enter the target domain (example: example.com): example.com
```

## 📝 Examples

### Regular Mode Output
```json
        "ip": "20.205.243.166",
        "ip_details": {
            "status": "success",
            "country": "Singapore",
            "countryCode": "SG",
            "region": "01",
            "regionName": "Central Singapore",
            "city": "Singapore",
            "zip": "168812",
            "lat": 1.283,
            "lon": 103.833,
            "timezone": "Asia/Singapore",
            "isp": "Microsoft Corporation",
            "org": "Microsoft Azure Cloud (southeastasia)",
            "as": "AS8075 Microsoft Corporation",
            "query": "20.205.243.166"
```



> 🎯 **Best Practice**: Always verify findings through multiple sources!

### 🔒 [Password Checker](https://github.com/rexzea/Simple-password-strength-checker)
#### Features 
Password Strength Checker is a Python application designed to analyze and evaluate password strength in depth. This project aims to provide an assessment of password security using various metrics and analytical algorithms in Python.

##### Key Features
  - Password Complexity Analysis
  - Password Length Checking
  - Password Entropy Calculation
  - Weak Password Identification
  - Password Strength Scoring
  - Security Recommendations
  - Objectives

##### This project aims to:
  - Help you create strong passwords
  - Enhance digital security awareness
  - Provide an easy guide for password creation

    
##### Prerequisites
Python 3.7+
No additional external libraries required

### 🔐 [AES Text Encryptor](https://github.com/rexzea/AES-Text-Encryptor) 
**AES Text Encryptor** is a Python application that allows you to encrypt and decrypt text messages using the **AES (Advanced Encryption Standard)** algorithm. With encrypted storage in SQLite database, you can manage messages securely and efficiently! 

##### Main Features
-  **Message Encryption**: Encrypt text messages with a password using the AES algorithm
-  **Message Decryption**: Decrypt encrypted messages with the correct password
-  **Database Storage**: Encrypted messages are stored in SQLite with metadata for reference
-  **Key Security**: Encryption keys are generated using PBKDF2 for additional security
-  **Activity Logging**: Application activities are automatically recorded in log files for monitoring

##### 📦 Installation
 Create a virtual environment (optional but recommended):
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # For Linux/MacOS
   myenv\Scripts\activate     # For Windows
   ```

#### How to Use
##### 1. Run the program:
```bash
python AES.py
```

##### 2. Choose one of the menu options:
  - 1: Encrypt a new message
  - 2: Decrypt an encrypted message
  - 3: View list of saved messages
  - 4: Exit application

#### Technologies Used
Python 3.10+
- Cryptography: For message encryption and decryption
- SQLite: As local database storage
- Logging: For recording application activities

#### To find out the results of this project preview, please [click here!](https://github.com/rexzea/AES-Text-Encryptor) 

> 💡 **Tip**: Use CBC mode for enhanced security in most scenarios!

### 🎲 [Secure Password Generator](https://github.com/rexzea/SecurePass-Generator)
#### Project Description
A tool to generate strong passwords and secure your sensitive data. This project provides solutions for password creation and security using encryption technology.

#### Key Features
- **Smart Password Generator**
  - Highly secure random password generation
  - Full control over password complexity
  - Reliable generation algorithm (error-free)
- **Advanced Encryption Methods**
  - Support for multiple hash algorithms
  - Password conversion to encrypted format
  - Password strength analysis
  - Protection against brute force attacks


#### Technologies
- Encryption Algorithms:
  - SHA-256
  - BCrypt
  - PBKDF2
- Programming Language: Python

#### Security
- No storage of raw passwords
- End-to-end encryption
- Maximum data protection

### SecurePass Generator & HASH Encryption
#### What Is HASH Encryption?
HASH encryption is the process of converting data into a unique **one-way** code. This means:
- Once data is converted to HASH, it's virtually impossible to revert to its original form
- Each different input will generate a different HASH
- Small changes in input will result in completely different HASH outputs

#### Why Use HASH?
- **Non-Reversible**: No mathematical way to "decode" HASH back to original text
- **Secure**: Each character combination produces a different HASH
- **Consistent**: Same input always produces the same HASH

#### HASH Decryption Methods
To "crack" a HASH, attackers must use:
1. **Brute Force Attack**
   - Try all possible combinations
   - Can take thousands/millions of years
   - Highly inefficient
2. **Rainbow Table Attack**
   - Pre-processed tables of various HASH combinations
   - Modern techniques like "salt" make this method ineffective
3. **Online Decryption Services**
     Using websites like
     ```bash
     https://crackstation.net/
     ```
     Or
     ```bash
     https://hashes.com/
     ```
   - Only effective for common/weak HASHes
   - No guarantee of successful decryption

#### Password Storage Tips : 
**MANDATORY: Store Original Passwords Safely**
- Use encrypted password managers
- Write in personal notebook
- Store in hidden location
- **NEVER** store passwords in:
  - Email
  - Computer files
  - Unencrypted cloud storage

#### HASH Process Example
```
Input: "Admin123!"
HASH SHA-256: 
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

#### Best HASH Methods
- SHA-256
- BCrypt
- Argon2
- PBKDF2

#### Important Warnings
- HASH is designed NOT to be reversible
- Always store original passwords securely like on paper or notes
- Use complex character combinations

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
