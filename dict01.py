#!/usr/bin/env python3

switch = {'hostname' : 'sw1', 'ip':'10.0.1.1', 'version':  '1.2', 'vendor':'cisco'}

print(switch['hostname'])

print(switch['ip'])

#print(switch['lynx'])

print("First test - .get()")
print(switch.get('lynx'))

print("Second Test - .get()")
print(switch.get('lynx',"THE KEY IS IN ANOTHER CASTLE!"))

print("Third Test - .get()")
print(switch.get('version'))


print("Fourth Test - .keys()")
print(switch.keys())

print("Fifth Test - .values()")
print(switch.values())

print("Sixth Test - .pop()")
switch.pop('version')
print(switch.keys())
print(switch.values())

print("Sevent Test - ADD a new value")
switch['adminlogin'] = 'karl08'
print(switch.keys())
print(switch.values())

print("Eigth Test - ADD a new value")
switch['password'] = 'qwerty'
print(switch.keys())
print(switch.values())


