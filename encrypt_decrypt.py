#! /usr/bin/python3
import base64

data = {'showpassword':'no','bgcolor':'#ffffff'}

#for key in data:
#	print(data[key])


def xorencrypt(item):
	key = base64.base64.decode('')
	output = ""
	index = 0
	for item in x:
    		output += chr(ord(item) ^ ord(key[index]))
    		index = (index + 1)%len(key)
	return output


