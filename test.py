#!/bin/python
#test
ip = raw_input("vvedi diapzon ip:")
a = ip.split('-')
div = [a[0]]
l_a = a[1].split('.')
f_a = a[0].split('.')
b = int(l_a[3]) - int(f_a[3])
for ips in range(b):
  f_a[3] = str(int(f_a[3]) + 1)
  div.append(".".join(f_a))
print (div)	
