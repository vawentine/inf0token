#!/usr/bin/python3
import requests, json, sys
from time import sleep

# Base variables
url = "https://discord.com/api/v9/users/@me"

# Check the token
def check_token(token):
	headers = {"Authorization": token}
	r = requests.get(url, headers=headers) # GET request to Discord API
	if r.status_code == 200:
		print("\n[+] Token passed verification check... gathering info")
		sleep(2)
	else:
		print(f"[!] Token invalid, Error: {r.status_code}")
		sys.exit()

# Gather info
def gather_info(token):
	check_token(token)
	sleep(2)
	headers = {"Authorization": token}
	r = requests.get(url, headers=headers) # GET request to Discord API
	data = r.json()
	verified = f"{data['email']} - Verified" if data["verified"] is True else f"{data['email']} - Not Verified"
	gauth_status = "Enabled" if data["mfa_enabled"] is True else "Disabled"

	print(f'''
[+] Account: {data['username']}#{data['discriminator']} - {data['id']}
[+] Phone Number: {data['phone']}
[+] Email: {verified}
[+] GAuth: {gauth_status}
		''')

def main():
	if len(sys.argv) < 2:
		print(f"{sys.argv[0]} TOKEN")
	else:
		token = sys.argv[1]
		gather_info(token)
		print("~ valentine\n")

if __name__ == "__main__":
	main()