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

#my_list= [1,2,7,9,454,344,2354543,34534534,4534543]
number = input("can you guess the number from my list?")



def check_number(n):
    print("You entered {0}".format(n))
    if (n.isnumeric() == False):
        print("Please enter number only")
        n1 = input("Try again..")
        check_number(n1)
    else:
        my_list = [1,2,7,9,343,3454,2343,2343,55,77]
        intNumber = int(n)
        print(my_list.count(intNumber))
        if (my_list.count(intNumber) > 0):
            print("You guessed it...")
        else:
            number = input("Try again..")
            check_number(number)

check_number(number)
