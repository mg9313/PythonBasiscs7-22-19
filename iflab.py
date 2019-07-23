#!/usr/bin/env python3

hostname = input("What is the hostname?")

if hostname.find("mtg") > 0:
    print("hostname has 'mtg' in it")
else:
    print("hostname is clear ")

ip = input("enter your IP")

if ip.count(".") != 3:
    print("It looks like IP is not valid")
else:
    print("IP looks good")


