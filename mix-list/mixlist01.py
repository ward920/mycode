#!/usr/bin/env python3

# create a list containing three items
my_list = [ "192.168.0.5", "UDP", 5060, "UP" ]

# display only the IP addresses to the screen.
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# display the first item in the list
#print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
#print("The second item in the list (Protocol): " + my_list[1] )

# display the third item in the list
#print("The third item in the list (port): " + str(my_list[2]) )

# display the fourth item in the list
#print("The last item in the list (state): " + my_list[3] )

# print the IP addresses
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# example 2 - use the comma separator
print("IP addresses:", iplist[3], ", and", iplist[4])

# example 3 - use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
