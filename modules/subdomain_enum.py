import requests
import json
from bs4 import BeautifulSoup

#optional: brute-force subdomains with a wordlist
def brute_force_subdomains(domain, wordlist_path="wordlist.txt"):
    found = []
    print(f"[+] starting brute-force on {domain} using {wordlist_path}")

    with open(wordlist_path, "r") as f:
        for word in f:
            subdomain = f"{word.strip()}.{domain}"
            url = f"https://{subdomain}"
            try:
                res = requests.get(url, timeout=3)
                if res.status_code < 400:
                    print(f"[+] Found: {subdomain}")
                    found.append(subdomain)
            except requests.exceptions.RequestException:
                continue
    return found

def enumerate_subdomains(domain):
    brute_subs = brute_force_subdomains(domain)
    return brute_subs

#crt.sh scrapping method
def get_subdomains_from_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        res = requests.get(url, timeout=5)
        data = res.json()
        subdomains = set()
        for entry in data:
            subdomains.update(entry['name_value'].split('\n'))
        return sorted(subdomains)
    except:
        return []
    
#combine both methods
def enumerate_subdomains(domain):
    print(f"[+] Enumerating subdomains for {domain}")
    subs = get_subdomains_from_crtsh(domain)
    print(f"[+] Found {len(subs)} from crt.sh")

    #optional: Uncommon if you have a wordlist
    #brute_subs = brute_force_subdomains(domain)
    #print(f"[+] Found {len(brute_subs)} from brute_force")
    #subs.extend(brute_subs)

    return list(set(subs))
