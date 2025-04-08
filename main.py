import argparse 
from modules.subdomain_enum import enumerate_subdomains
from modules.port_scanner import scan_ports 
from modules.banner_grab import grab_banners
from modules.cve_checker import check_vulnerabilities
from reports.report_generator import generate_report

parser = argparse.ArgumentParser(description="AutoreconX: A lightweight recon tool.")
parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
args = parser.parse_args()

if __name__ == "__main__":
    domain = args.domain

    # sub domain Enumeration
    subs = enumerate_subdomains(domain)
    print("\n=== Discovered Subdomains ===")
    for sub in subs:
        print(sub)

    # Port scanning on main domain
    open_ports = scan_ports(domain)
    print("\n=== Open Ports ===")
    for port in open_ports:
        print(f"Port {port} is open")

    # Banner Grabbing
    banners = grab_banners(domain, open_ports)
    print("\n=== Banners Collected ===")
    for port, banner in banners.items():
        print(f"Port {port}: {banner}")

    # CVE Lookup
    vulns = check_vulnerabilities(banners)
    print("\n=== Vulnerability Report ===")
    for port, cves in vulns.items():
        print(f"\nPort {port}:")
        if cves:
            for cve in cves:
                print(f" - {cve}")
        
        else:
            print("No known CVEs found.")

    # Generate report
    report= generate_report(domain, subs,open_ports, banners, vulns)

    # Print or save to file
    print(report)

    with open(f"{domain}_report.txt", "w") as f:
        f.write(report)
    print(f"\n[+] report saved to{domain}_report.txt")
