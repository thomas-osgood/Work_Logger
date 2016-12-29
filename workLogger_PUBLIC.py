#
# Created By: Thomas Osgood
# Date Created: 2016-03-29
# Purpose: Work Logger Program
#

#
# Required Imports
#
from datetime import datetime

#
# Global Variables
#
logfile = 'work_logger.csv'

#
# SysMsg Function
#
# Generates custom system message
#
def SysMsg(stringVar):
    print "[ ]{0:70}...".format(stringVar)
    return 0

#
# Log Function
#
# Saves timestamped string to logfile
#
def LogFunc(stringVar):
    logline = "{0},{1}\n".format(datetime.now(),stringVar)

    SysMsg("Opening Log")
    f = open(logfile, "a")
    f.write(logline)
    SysMsg("Write Successful")
    f.close()
    SysMsg("Log Closed")

    return 0

#
# Main Function
#
# Called each time program run
#
def Main():

    # Infinte loop until user enters exit char
    while(True):
        # Get Input From User
        action = raw_input("Action To Be Logged: (-1 to quit)\n> ")

        # Strip 'newline' character
        action = action.strip('\n')
        
        # Check for a -1 entered
        if (action == "-1"):
            break
        else:
            LogFunc(action)
    return 0

if __name__ == "__main__":
    SysMsg("Beginning Logging Program")
    Main()
    SysMsg("Program Shutting Down")
