import os
import requests
import logging

print("This is a Proxy Scrapper made by Team Coderunner for RowdyHacks 2024")
print("This is a simple program that pulls from the Proxyscrape API to get  proxies.")
print("This pulls from the Proxyscrape API to get the proxies.")

print("Proxies are useful for: Access Control, anonymization, and content filtering.")


# Print program logo
print("\033[95m" + """
░█████╗░░█████╗░██████╗░███████╗██████╗░██╗░░░██╗███╗░░██╗███╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░░░██║████╗░██║████╗░██║██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██║░░██║█████╗░░██████╔╝██║░░░██║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
██║░░██╗██║░░██║██║░░██║██╔══╝░░██╔══██╗██║░░░██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║╚██████╔╝██║░╚███║██║░╚███║███████╗██║░░██║
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
""" + "\033[0m")

def fetch_proxies(protocol):
    try:
        response = requests.get(f'https://api.proxyscrape.com/v2/?request=getproxies&protocol={protocol}&timeout=10000&country=all&ssl=all&anonymity=all')
        if response.status_code == 200:
            proxies = response.text.split('\r\n')
            return proxies
        else:
            logging.error(f"Failed to fetch proxies. Status code: {response.status_code}")
    except requests.RequestException as e:
        logging.error("Error fetching proxies:", exc_info=True)
    return []

def save_proxies_to_file(proxies, filename):
    try:
        with open(filename, 'w') as f:
            for proxy in proxies:
                f.write(proxy + '\n')
        logging.info(f"Proxies saved to {filename}")
    except IOError as e:
        logging.error("Error saving proxies to file:", exc_info=True)

def main():
    logging.basicConfig(filename='proxy_fetcher.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    # Get current directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Fetch proxies of the desired protocol
    while True:
        protocol = input("Enter protocol (http, socks4, socks5): ").lower()
        if protocol in ['http', 'socks4', 'socks5']:
            break
        else:
            print("Invalid protocol. Please enter 'http', 'socks4', or 'socks5'.")

    proxies = fetch_proxies(protocol)

    if proxies:
        # Save proxies to file in the same directory as the script
        filename = os.path.join(script_dir, f'{protocol}_proxies.txt')
        save_proxies_to_file(proxies, filename)
        print("Proxies fetched and saved successfully.")
    else:
        print("No proxies fetched. Please check the logs for more information.")

if __name__ == "__main__":
    main()

