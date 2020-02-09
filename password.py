#!/bin/python
import re

pas = raw_input("vvedi password:")
a = re.match(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$',pas)
print(a)
if a!=None:
	print ("Ok")
else: print ("No ok!")
