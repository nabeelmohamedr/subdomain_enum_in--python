import requests
import threading
import re

def is_valid_domain(domain):
    # Basic domain format validation using regex
    pattern = re.compile(
        r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.'
        r'[A-Za-z]{2,6}$'
    )
    return pattern.match(domain)

def is_domain_reachable(domain):
    try:
        response = requests.get(f'http://{domain}', timeout=5)
        return True
    except requests.RequestException:
        return False

# Take domain input from user
while True:
    domain = input("Enter the target domain (example: youtube.com): ").strip()

    if not is_valid_domain(domain):
        print("Invalid domain format. Please enter a valid domain like 'example.com'.")
        continue

    if not is_domain_reachable(domain):
        print(f"Cannot reach the domain {domain}. Please check the domain or your internet connection.")
        continue

    break  # Domain is valid and reachable

# Read subdomains from file
with open('subdomains.txt') as file:
    subdomains = file.read().splitlines()

discovered_subdomains = []
lock = threading.Lock()

def check_subdomain(subdomain):
    url = f'http://{subdomain}.{domain}'
    try:
        requests.get(url, timeout=3)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomain:", url)
        with lock:
            discovered_subdomains.append(url)

threads = []

for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Save discovered subdomains to a file
with open("discovered_subdomains.txt", 'w') as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)

print("Scan completed. Results saved in discovered_subdomains.txt")
