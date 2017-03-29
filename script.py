#!/usr/bin/python
#import interop_client_lib
from sys import version_info
python_version = version_info[0]
print python_version
#Here's a comment
'''
This script has only been tested in Python 2 as of now.

This script is responsible for communications between the interoperability server and the plane, and between the 
It takes telemetry data from the plane and uploads it to the server.
- This data is sent over the mavlink protocol. 
-Both this program and qgroundcontrol need to access the same mavlink stream, so this program will create a new process
 using mavproxy to split the incoming stream into two streams. 
- When this program finishes running, it needs to kill the process running mavproxy

It also takes obstacle position data from the interoperability server and outputs it to the console. 
- This will allow the pilot to manually plot the obstacle locations on qgroundcontrol and then avoid them.  
- Future versions of this program might upload the data to a modified version of qgroundcontrol, which would 
display those obstacles onscreen

'''

#The host name and port number will be specified at the competition. For testing, use localhost as the name and 8080 for the port
confirmed_hostname_and_portnum=False

if python_version==2:
	while not confirmed_hostname_and_portnum:
		print "using Python 2"
		hostname = raw_input("Please enter the host name: ")
		portnum = raw_input("Please enter the port number: ")
		confirmation_prompt = "Host name is " + hostname + " and port number is " + portnum + ". (y to confirm): "
		confirm = raw_input(confirmation_prompt)
		if confirm=='y' or confirm=='Y':
			confirmed_hostname_and_portnum=True


elif python_version==3:
	while not confirmed_hostname_and_portnum:
		print "using Python 3"
		hostname = input("Please enter the host name: ")
		portnum = input("Please enter the port number: ")
		confirmation_prompt = "Host name is " + hostname + " and port number is " + portnum + ". (y to confirm): "
		confirm = input(confirmation_prompt)
			if confirm=='y' or confirm=='Y':
				confirmed_hostname_and_portnum=True


