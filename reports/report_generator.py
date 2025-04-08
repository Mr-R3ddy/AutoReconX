def generate_report(domain, subdomains, ports, banners, cves):
    report = []
    report.append(f"\nRecon Report fro {domain}")
    report.append("=" * 50)

    report.append("\n1. Subdomains Discovered:")
    if subdomains:
        for sub in subdomains:
            report.append(f" - {sub}")
    else:
        report.append(" - No subdomains found.")

    report.append("\n2. Open Ports:")
    if ports:
        for port in ports:
            banner = banners.get(port, "Unknown service")
            report.append(f" - Port {port}: {banner}")
    else:
        report.append(" - No open ports found.")
    
    report.append("\n3. Vulnerabilities (CVEs):")
    if cves:
        for port, cve_list in cves.items():
            report.append(f"\n Port {port}:")
            if cve_list:
                for cve in cve_list:
                    report.append(f" - {cve}")
            else:
                report.append(" -No known CVEs.")
    else:
        report.append(" -CVE data nor available.")

    report.append("\n" + "=" * 50)
    return "\n".join(report)