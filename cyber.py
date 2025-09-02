from colorama import init, Fore, Style
import os
import time
import requests

init()


def display_banner():
    banner = """
    ****************************************
    *     😈 CYBERSHADOW v1.0 😈         *
    *      (Shadow of the Dark)      *
    ****************************************
    """
    print(Fore.RED + banner + Style.RESET_ALL)


def display_info():
    print(Fore.GREEN + "Community: DARK" + Style.RESET_ALL)
    print(Fore.GREEN + "Author: AMIT" + Style.RESET_ALL)
    print(Fore.YELLOW + "---------------------------------------" + Style.RESET_ALL)


def ip_lookup():
    url = input(Fore.CYAN + "\nEnter website URL (e.g., google.com, no https://): " + Style.RESET_ALL)
    try:
        response = requests.get(f"http://ip-api.com/json/{url}")
        data = response.json()
        if data["status"] == "success":
            print(Fore.MAGENTA + "\nIP Lookup Results:" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"IP Address: {data['query']}" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"Country: {data['country']}" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"City: {data['city']}" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"ISP: {data['isp']}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "\nError: Could not fetch IP details! (Check domain)" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"\nError: {e}" + Style.RESET_ALL)
    input(Fore.CYAN + "\nPress Enter to continue..." + Style.RESET_ALL)


def menu():
    while True:
        os.system("clear")  
        display_banner()
        display_info()
        print(Fore.BLUE + "1. Start (IP Lookup)" + Style.RESET_ALL)
        print(Fore.BLUE + "2. Exit" + Style.RESET_ALL)
        choice = input(Fore.YELLOW + "Enter your choice (1-2): " + Style.RESET_ALL)

        if choice == "1":
            print(Fore.GREEN + "\nStarting CYBERSHADOW - IP Lookup Mode..." + Style.RESET_ALL)
            time.sleep(1)
            ip_lookup()
        elif choice == "2":
            print(Fore.RED + "\nExiting CYBERSHADOW. Stay Dark! 👾" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\nInvalid choice! Try again." + Style.RESET_ALL)
            time.sleep(1)


if __name__ == "__main__":
    menu()