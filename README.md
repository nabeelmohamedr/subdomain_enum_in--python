
---

# Subdomain Enumeration Tool in Python

## About the Program

This Python project is a **Subdomain Enumeration Tool** that helps identify active subdomains of a target website using a wordlist.

It is useful for:

* Penetration Testing
* Ethical Hacking
* Bug Bounty Hunting
* Web Application Security Assessments

The program utilizes:

* User input for the target domain
* Validation to check if the domain is correctly formatted and reachable
* Multi-threading for fast subdomain scanning
* File output to save the discovered subdomains

---

## Applications

* **Subdomain Enumeration:** Find hidden or less-known subdomains that could lead to security weaknesses
* **Web Application Mapping:** Build a comprehensive structure of a website
* **Bug Bounty Hunting:** Discover hidden endpoints that might be exploitable
* **Security Audits:** Assess the scope of web assets for large organizations

---

## Skills Learned

* **Python fundamentals:** loops, functions, file handling
* **Regular expressions:** for input validation
* **HTTP requests:** using the `requests` library
* **Multi-threading:** for concurrent execution
* **Safe thread management:** using locks
* **Basic security concepts:** like subdomain enumeration and target discovery
* **Command-line input/output management**

---

## 🖥️ How to Use or Run the Tool

### 1. Clone the Repository
```bash
git clone https://github.com/nabeelmohamedr/subdomain_enum_in--python.git
cd subdomain_enum_in--python
```

### 2. Prepare the Subdomain Wordlist
Ensure you have a `subdomains.txt` file in the same directory. Example content:
```
www
mail
ftp
api
blog
test
admin
cdn
dev
shop
```

### 3. Install Required Python Module
```bash
pip install requests
```

### 4. Run the Program
```bash
python subdomain_enum.py
```
When prompted:

```
Enter the target domain (e.g., youtube.com): example.com
```

The tool will scan subdomains and display discovered ones:
```
[+] Discovered subdomain: http://blog.example.com
[+] Discovered subdomain: http://shop.example.com
...
Scan completed. Results saved in discovered_subdomains.txt
```

### 5. Output File
All discovered subdomains will be saved in:
```
discovered_subdomains.txt
```

## 🔗 Subdomain Wordlist Source
- **SecLists GitHub Repository** — Discovery/DNS  
  [https://github.com/danielmiessler/SecLists](https://github.com/danielmiessler/SecLists)  
  Contains common subdomains gathered from real-world penetration testing and security research.

## ✅ Requirements
- Python 3.x
- `requests` Python library (`pip install requests`)

## 💡 Future Improvements
- Add HTTPS subdomain checking
- Incorporate progress bar display using [`tqdm`](https://tqdm.github.io/)
- Use asynchronous requests for ultra-fast scanning
- Add customizable thread limits and delay settings

## ⚙️ License
This project is open-source and available under the MIT License.



**Happy Security Testing!** 🚀



