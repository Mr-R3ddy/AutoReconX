import socket

def grab_banner(ip_or_domain, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip_or_domain, port))
        sock.send(b"\r\n") # sen something to get a response
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return None 
    
def grab_banners(ip_or_domain, open_ports):
    print(f"\n[+] Grabbing banners from {ip_or_domain}")
    banners = {}

    for port in open_ports:
        banner = grab_banner(ip_or_domain, port)
        if banner:
            print(f"[+] Port {port}: {banner}")
            banners[port] = banner
        else:
            print(f"[-] Port {port}: No banner or timeout")
        
        return banners 