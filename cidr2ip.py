#!/usr/bin/python
'''
Author: SAINTz

'''

from netaddr import *

f_output = open("everyip.txt", "w")
f_in = open('ipcidr.txt','wb')
inputs = f_in.readlines()
for cidrs in inputs:
    #ip = IPNetwork('10.0.0.0/8')
    ip = IPNetwork(cidrs)
    for addr in ip:
        f_output.write(str(addr) + '\n')

f_output.close()
f_in.close()