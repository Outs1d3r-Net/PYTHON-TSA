#!/usr/bin/python

#############################
### THE SERPENT AWAKENING ###
#############################

#LIBRARIES

import os
import sys
import commands

while True:
    eXit = 0
    #input("[0]==> Exit")
    up="2018-09-02-18.42.25" #YEAR - MONTH - DAY - HOUR - MINUTES - SECONDS
    locks=commands.getoutput("date +%Y-%m-%d-%H.%M.%S") #CLOCK
    if locks == up: #CHECKER
        while True:
            os.system("mplayer alarm.mp3")
    elif eXit == 1:
        sys.exit(0)
    else:
        os.system("clear")
        print "CURRENT TIME:-->",locks,"||| AWAKENING:-->",up
        os.system("sleep 1"); #COUNTER
