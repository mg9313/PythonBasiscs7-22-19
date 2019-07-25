#!/usr/bin/env python3

configfile = open("vlanconfig.cfg", "r")

configblog = configfile.read()

lines_cnt = configblog.find("\n")

configlist = configblog.splitlines()


print("{} no. of lines in config file".format(lines_cnt))

print(configlist)

configfile.close()

