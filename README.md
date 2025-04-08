# AutoReconX
a lightweight automated reconnaissance tool written in python for ethical hackers and cybersecurity proffesionals.
It performs subdomain enumeration, port scanning, banner grabbing, CVE lookup, and generates a proffesional recon report.

------

## features

- Subdomain enumeration (using a custom wordlist)
- toip port scanning (TCP)
- Banner grabbing from open ports
- CVE lookup using Vulners API
- AI-style natural language recon report
- Command-Line interface

-------

## Folder Structure

AutoReconX/
 |---- main.py
 |---- modules/
|  |-----subdomain_enum.py
|  |-----port_scanner.py
|  |-----banner_grab.py
|  |-----cve_checker.py
|  |-----report_generator.py
 |---- wordlist/
|  |-----subdomains.txt
 |---- requirements.txt
 |---- README.md

 ---------

## Author
Sai 
Cybersecurity Enthusiast | Ethical hacking | Python Developer

## Installation

Clone the repository:
```bash
git clone https://github.com/Mr-R3ddy/AutoReconX.git
cd AutoReconX
pip install -r requirements.txt
python main.py -d example.com


## usage

```bash
python main.py -d example.com

