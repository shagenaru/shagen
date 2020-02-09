#!/bin/python
import re

def stripus(wor,st):
	if st == '':
		print (re.findall(r'[^\s]', wor))
	else:
		print (re.findall(r'[^{}]'.format(st),wor))
a = raw_input("vvedi a: ")
b = raw_input ("vvedi b: ")
stripus(a,b)
