#!/usr/bin/env python3
'''module that deals with functions'''

def commandpush(devicecmd): #devicecmd=list
    ''' push commands to devices '''
    for coffeetime in devicecmd.keys():
        print("Handshaking......connecting with " + coffeetime)
        for mycmds in devicecmd[coffeetime]:
            print("Attempting to sending command --> " + mycmds)
        print("\n")

def betterpush(filename): #file name having ip and commands
    '''better push commands to devices'''
    fstream = open(filename, "r")
    #lines = fstream.readlines()
    for l_a in fstream:
        #print(l)
        s_a = str(l_a).strip()
        #print(s)
        print(s_a.isnumeric())
        #if s.isalpha()== True:
           # print("Attempting to sending command --> " + s, end="")
        #else:
           # print("Handshanking....connecting with " + s, end="")

def deviceboot(iplist): #list of IPs
    '''boot list of IPs '''
    for ip_a in iplist:
        print("Connecting to... " + ip_a)
        print("Rebooting NOW!...")



def main():
    ''' main function '''
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"],
               "10.2.0.1":["interface eth1/1", "shutdown"]}
    iplist = ["10.1.0.1", "10.2.0.1"]
    work2do_file = "work2do.txt"

    print("Welcome to the network device command pusher") # welcome message
    #get data set
    print("\nData set found\n") # replace with function call that reads in data from file
    betterpush(work2do_file)
    print("\n")
    ##run commandpush
    commandpush(work2do) # call function to push commands to devices

    #run deviceboot
    deviceboot(iplist)

#call main function
main()
