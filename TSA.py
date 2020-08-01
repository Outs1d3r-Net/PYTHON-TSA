#!/usr/bin/env python2

#############################
### THE SERPENT AWAKENING ###
#############################

#LIBRARIES
import os
import sys
import commands

os.system('clear')

#DEPENDENCIES
mplayer = os.system('which mplayer')
if mplayer == 256:
    c = raw_input('[*] Dependencies [*]\n\nmplayer not installed, for the alarm clock to work properly please install the mplayer program\n[+] Y for install\n[-] N for exit\n>>> ').strip('\n')
    if c == 'Y' or c == 'y':
        if os.geteuid() !=0:
            print 'Error ! required root privilege.'
            sys.exit(1)
        os.system('apt install mplayer -y')
        os.system('clear')
        print 'End ! Now run the program without root privileges!'
        sys.exit(0)
    elif c == 'N' or c == 'n':
        print 'bye bye...'
        sys.exit(1)
    else:
        print 'Option not allowed !'
        sys.exit(1)


#MAIN
os.system('clear')
up = raw_input("Please select data in format: 2020-08-01-07.40.42 (Year-month-day-hour-minutes-seconds)>>> ")
    #EX: 2020-08-01-07.40.42 HIGHLIGHTER - [YEAR - MONTH - DAY - HOUR - MINUTES - SECONDS]
    #Please change this field to the date and time of your preference.

while True:

    locks=commands.getoutput("date +%Y-%m-%d-%H.%M.%S") #CLOCK
    if locks == up: #CHECKER
        while True:
            os.system("mplayer alarm.mp3")
    else:
        os.system("clear")
        print "CURRENT TIME:-->",locks,"||| AWAKENING:-->",up
        os.system("sleep 1"); #COUNTER
