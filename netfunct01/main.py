#!/usr/bin/env python3

def commandpush(devicecmd): #devicecmd=list
    for coffeetime in devicecmd.keys():
        print("Handshaking......connecting with " + coffeetime)
        for mycmds in devicecmd[coffeetime]:
            print("Attempting to sending command --> " + mycmds)
        print("\n")

def betterpush(filename): #file name having ip and commands
    fstream = open(filename,"r")
    #lines = fstream.readlines()
    for l in fstream:
        #print(l)
        s = str(l).strip()
        #print(s)
        print(s.isnumeric())
        #if s.isalpha()== True:
           # print("Attempting to sending command --> " + s, end="")
        #else:
           # print("Handshanking....connecting with " + s, end="")

def deviceboot(iplist): #list of IPs 
    for ip in iplist:
        print("Connecting to... " + ip)
        print("Rebooting NOW!...")



def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"]}
    iplist = ["10.1.0.1", "10.2.0.1"]
    work2doFile = "work2do.txt"

    print("Welcome to the network device command pusher") # welcome message

    #get data set
    print("\nData set found\n") # replace with function call that reads in data from file
    
    betterpush(work2doFile)
    print("\n")
    ##run commandpush
    commandpush(work2do) # call function to push commands to devices

    #run deviceboot
    deviceboot(iplist)

#call main function
main()
        
