#!/usr/bin/env python3

configfile = open("vlanconfig.cfg", "r")

#print(configfile.read())

configlist = configfile.readlines()

print(configlist)

for x in configlist:
    print(x.strip(), end="")

configfile.close()

