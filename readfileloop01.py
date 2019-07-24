#!/usr/bin/env python3

dnsfile = open("dnsservers.txt")

dnslist =  dnsfile.readlines()

for s in dnslist:
    print(s, end="")
dnsfile.close()
