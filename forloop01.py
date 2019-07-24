#!/usr/bin/env python3

print("\n Enter the number of rows..")
rows = input()
print("\n Enter the number of columns...")
cols = input()

def print_stars(rows,cols):
    r = int(rows)
    c = int(cols)
    for i in range(r):       
        print(" ")
        for j in range(c):
            print("*",end="")
        c = c - 1
        
    print("\n Done printing stars")

print_stars(rows, cols)


    

