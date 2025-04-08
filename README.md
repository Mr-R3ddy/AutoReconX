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
 
## usage

```bash
python main.py -d example.com

