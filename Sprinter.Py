#A python sprint counter
#Zijing Zhang
#12-02-2017
import sys
import string
from time import sleep

def timer(minutes,BeepTimes):
    if minutes < 0:
        print "Invalid value for minutes, should be >= 0"
        sys.exit(1)

    seconds = minutes * 60

    if minutes == 1:
        unit_word = " minute"
    else:
        unit_word = " minutes"

    try:
        if minutes > 0:
            print "Sleeping for " + str(minutes) + unit_word
            sleep(seconds)
        print "Time is up!"
        for i in range(BeepTimes):
            print chr(7),
            print i+1
            sleep(1)
    except KeyboardInterrupt:
        print "Interrupted by user"
        sys.exit(1)

#sprinter
#    precondition
#        concole start input
#    postcondition
#        calls timer with 7 minutes and 21 chime times
#        print out sprint name
#        print out cycle start and end
def sprinter(SprintName):
    print SprintName+" starts!"
    timer(7,21)
    print SprintName+ " ends!"

#main
print "Cycle starts!"
for i in range(3):
    SprintName="Sprint "+str(i+1)
    sprinter(SprintName)
print "Cycle ends!"
