#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - testing if strings test true"""

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.") # indented under if
elif ipchk: # if any data is provided, this will test true
    print("Looks like the IP address was set: " + ipchk) # indented under elif
else:   #if data is not provided
    print("You did not provide input.") # indented under else

