import socket
from concurrent.futures import ThreadPoolExecutor

#common top ports (you can expand this list)
TOP_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389, 8080, 8443]

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return port
    except:
        pass
    return None

def scan_ports(ip_or_domain):
    print(f"[+] scanning ports on {ip_or_domain}")
    open_ports = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_port, ip_or_domain, port) for port in TOP_PORTS]
        for future in futures:
            port = future.result()
            if port:
                print(f"[+] Port {port} is open")
                open_ports.append(port)

    return open_ports 