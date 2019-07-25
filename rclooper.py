#!/usr/bin/env python3

import csv

with open("csv_users.txt", "r") as f:
    i = 0
    for row in csv.reader(f):
        i = i+1
        #print(row)
        w = open("admin{}.rc".format(i), "a")
        print("export OS_AUTH_URL={}".format(row[0]), file=w)
        print("export OS_PROJECT_NAME={}".format(row[1]), file=w)
        print("export OS_PROJECT_DOMAIN_NAME={}".format(row[2]), file=w)
        print("export OS_USERNAME={}".format(row[3]), file=w)
        print("export OS_USER_DOMAIN_NAME={}".format(row[4]), file=w)
        print("export OS_PASSWORD={}".format(row[5]), file=w)
        w.close()

print("done creating admin rc files.")



