#!/usr/bin/python
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



#The host name and port number will be specified at the competition. For testing, use localhost as the name and 8000 for the port
confirmed_hostname_and_portnum=False
confirmed_username_and_password=False

if python_version==2:
	print "using Python 2"
	while not confirmed_hostname_and_portnum:
		hostname = raw_input("Please enter the host name: ")
		portnum = raw_input("Please enter the port number: ")
		url_confirm = raw_input("Host name is " + hostname + " and port number is " + portnum + ". (y to confirm): ")
		if (url_confirm=='y' or url_confirm=='Y'):
			confirmed_hostname_and_portnum = True

	while not confirmed_username_and_password:
		username = raw_input("Please enter your username: ")
		password = raw_input("Please enter your password: ")
		login_confirm = raw_input("Username is " + username + " and password is " + password + ". (y to confirm): ")
		if (login_confirm=='y' or login_confirm=='Y'):
			confirmed_username_and_password=True


elif python_version==3:
	print "using Python 3"
	while not confirmed_hostname_and_portnum:
		hostname = input("Please enter the host name: ")
		portnum = input("Please enter the port number: ")
		url_confirm = input("Host name is " + hostname + " and port number is " + portnum + ". (y to confirm): ")
		if (url_confirm=='y' or url_confirm=='Y'):
			confirmed_hostname_and_portnum = True

	while not confirmed_username_and_password:
		username = input("Please enter your username: ")
		password = input("Please enter your password: ")
		login_confirm = input("Username is " + username + " and password is " + password + ". (y to confirm): ")
		if (login_confirm=='y' or login_confirm=='Y'):
			confirmed_username_and_password=True


import interop_client_lib
url = "http://" + hostname + ":" + portnum 
print url
#client = interop.AsyncClient(url, )



