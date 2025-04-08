from vulners import Vulners

# Create a free account at vulners.com to get your API key
API_KEY = "XZY4K1FSYD8YX59JZ8OEDBTZ0Q0Q6WTPNTLFAPH8KWCLV8T1Y84BYGSXPSG6630Y" # Replace this

vulners = Vulners(api_key=API_KEY)

def check_vulnerabilities(banners):
    cve_results = {}

    print("\n[+] Checking for known vulnerabilities....")
    for port, banner in banners.items():
        try:
            print(f"[*] Searching CVEs for: {banner}")
            results = vulners.search(banner)
            cves = [r['id'] for r in results if 'id' in r and r['id'].startswith("CVE")]
            cve_results[port] = cves[:5]  # Limit to top 5 results
        except Exception as e:
            print(f"[-] Error on port {port}: [e]")
            cve_results[port] = []

    return cve_results 