#!/usr/bin/env python3

with open("keystone.common.wsgi") as fstream:

    lines = fstream.readlines()
    auth_fail_cnt = 0
    listIPs = []
    login_success_cnt = 0
    for l in lines:
        #print(l)
        if "- - - - -] Authorization" in l:
            auth_fail_cnt += 1
            if "from" in l:
                temp_list = l.split("from")
                listIPs.append(temp_list[1].strip("\n"))
                temp_list = []
        elif "-] Authorization" in l:
            login_success_cnt += 1

      

print("Authentication failed {} no. of times".format(auth_fail_cnt))
print(listIPs)
print("Successful login {} no. of times".format(login_success_cnt))



