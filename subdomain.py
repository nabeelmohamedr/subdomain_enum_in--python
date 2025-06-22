# Import required libraries
import requests     # To make HTTP requests to the subdomains
import threading    # To use multi-threading for faster subdomain scanning
import re           # For validating domain formats using regular expressions

# Function to validate if the entered domain has a correct format
def is_valid_domain(domain):
    # Basic domain validation pattern (example.com, google.in)
    pattern = re.compile(
        r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.'   # Domain name: cannot start/end with '-'
        r'[A-Za-z]{2,6}$'                     # Domain extension: 2 to 6 characters
    )
    return pattern.match(domain)

# Function to check if the entered domain is reachable (online)
def is_domain_reachable(domain):
    try:
        # Try sending a simple HTTP GET request
        response = requests.get(f'http://{domain}', timeout=5)
        return True  # If response is received, domain is reachable
    except requests.RequestException:
        return False  # Any exception means domain is unreachable

# Step 1: Ask the user to enter a target domain
while True:
    domain = input("Enter the target domain (example: youtube.com): ").strip()

    # Step 2: Validate the domain format using regex
    if not is_valid_domain(domain):
        print("Invalid domain format. Please enter a valid domain like 'example.com'.")
        continue  # Ask again if invalid

    # Step 3: Check if the domain is reachable (online)
    if not is_domain_reachable(domain):
        print(f"Cannot reach the domain {domain}. Please check the domain or your internet connection.")
        continue  # Ask again if unreachable

    break  # Exit loop if domain is valid and reachable

# Step 4: Read the list of potential subdomains from the file
with open('subdomains.txt') as file:
    subdomains = file.read().splitlines()

# Step 5: Create an empty list to store discovered (active) subdomains
discovered_subdomains = []

# Step 6: Create a threading lock to ensure safe writing to the list by multiple threads
lock = threading.Lock()

# Step 7: Define the function that will check each subdomain
def check_subdomain(subdomain):
    url = f'http://{subdomain}.{domain}'  # Build the full URL to check
    try:
        # Try sending an HTTP GET request to the subdomain
        requests.get(url, timeout=3)
    except requests.ConnectionError:
        pass  # If the subdomain is not found, ignore and continue
    else:
        # If no error, the subdomain exists
        print("[+] Discovered subdomain:", url)
        with lock:
            discovered_subdomains.append(url)  # Safely add to the list

# Step 8: Create and start a separate thread for each subdomain check
threads = []

for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()            # Start the thread
    threads.append(thread)    # Keep track of all threads

# Step 9: Wait for all threads to finish (synchronize)
for thread in threads:
    thread.join()

# Step 10: Save the list of discovered subdomains to a result file
with open("discovered_subdomains.txt", 'w') as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)  # Write each subdomain to the file

# Step 11: Notify the user that the scan is complete
print("Scan completed. Results saved in discovered_subdomains.txt")
