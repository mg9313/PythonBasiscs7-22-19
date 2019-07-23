#!/usr/bin/env python3

def main():
    ''' Run-time code'''
    #create a small string
    lilstring = "Alta3 Reasearch offers classes on Python coding"
    newlist = lilstring.split(" ")
    print(newlist)

    iplist = ["192","168","01","1"]
    singleip = ".".join(iplist)
    print(singleip)

main()

