# timer.py
# Zijing Zhang
import sys
import string
from time import sleep
TerminalArguments = sys.argv

if len(TerminalArguments) != 3:
    print "Usage: python timer.py duration_in_minutes beep_time"
    print "Example: python timer.py 10 10"
    print "Use a value of 0 minutes for testing the alarm immediately."
    print "Beeps given times after the duration is over."
    print "Press Ctrl-C to terminate the alarm clock early."
    sys.exit(1)

try:
    minutes = int(TerminalArguments[1])
    BeepTimes= int(TerminalArguments[2])
except ValueError:
    print "Invalid numeric value (%s) for minutes" % TerminalArguments[1]
    print "Should be an integer >= 0"
    sys.exit(1)

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

# EOF
