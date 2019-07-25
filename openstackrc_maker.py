#!/usr/bin/env python3

outFile = open("admin.rc", "a")
osAUTH = input("OS_AUTH_URL?")
print("export OS_AUTH_URL=" + osAUTH, file=outFile)

print("export OS_IDENTITY_API_VERSION=3", file=outFile)

outFile.write("written using outFile object")

outFile.close()
