#!/usr/bin/env python3

list1 = ['cisco-nxos', 'arista_eos', 'cisco-ios']
print(list1)

print(list1[1])

list1.extend(['juniper'])
print(list1)

list1.append(['10.1.0.1','10.2.0.1','10.3.0.1'])

print(list1)

print("4th element in list1 is ".format(list1[4]))

print(list1[4][0])




