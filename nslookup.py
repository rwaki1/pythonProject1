import os
import sys
import socket\

results_file = open("result.csv", "w")
file = 'IP_LIST.txt'
f = open(file, 'r')
lines = f.readlines()
f.close()
for i in lines:
    host = i.strip()
    output = ("%s - %s" % (host, socket.getfqdn(host)))
    results_file.write(output + "\n")
