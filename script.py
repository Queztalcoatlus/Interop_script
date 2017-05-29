#!/usr/bin/python
#import interop_client_lib 
from interop import AsyncClient
import signal

#import MAVProxy
#from pymavlink import mavutils
import os
import time
import threading #will need this later when I do multithreaded stuff

#check version
from sys import version_info
python_version = version_info[0]
print python_version


'''
This script is responsible for communications between the interoperability server and the ground station. 
It takes telemetry data from the plane and uploads it to the server.
- This data is sent over the mavlink protocol. 
- Both this program and qgroundcontrol need to access the same mavlink stream, so this program will create a new process
 using mavproxy to split the incoming stream into two streams. 
- When this program finishes running, it needs to kill the process running mavproxy

It also takes obstacle position data from the interoperability server and outputs it to the console. 
- This will allow the pilot to manually plot the obstacle locations on qgroundcontrol and then avoid them.  
- Future versions of this program might upload the data to a modified version of qgroundcontrol, which would 
display those obstacles onscreen.




Handling dependencies: 
When you try to run this script, you might get an error message that looks like the following: 

Traceback (most recent call last):
  File "./script.py", line 2, in <module>
    import interop_client_lib
  File "/Users/yaacovtarko/Desktop/UAS/Interop_script/interop_client_lib/__init__.py", line 1, in <module>
    from .client import Client
  File "/Users/yaacovtarko/Desktop/UAS/Interop_script/interop_client_lib/client.py", line 13, in <module>
    import requests
ImportError: No module named requests

If this happens, use Python's package manager to install the module that you're missing. Enter the line:
sudo pip install [missing package name] 
into the terminal, and then enter your password when prompted. In this case the command would be: 
sudo pip install requests



This script has only been tested in Python 2 as of now.
'''



#The host name and port number will be specified at the competition. For testing, use localhost as the name and 8000 for the port

'''
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
'''
#for testing
hostname="localhost"
portnum="8000"
username="testuser"
password="testpass"

mavlink_stream = "udp:127.0.0.1:14551"
usbport_id = "/dev/tty.usbserial-AL02UQVX"

url = "http://" + hostname + ":" + portnum 
print url

#launch mavproxy in a new process
#this will only work on a mac with mavproxy installed
mp_pid = os.fork()
if(mp_pid==0):
	args = ["mavproxy.py", "--daemon", "--out=udp:127.0.0.1:14551", "--out=udp:127.0.0.1:14552", "--master="+usbport_id]
	os.execvp("mavproxy.py", args)

#launch interop_cli.py in a new process
ic_pid = os.fork()
if(ic_pid==0): #new process
	args = ["interop_cli.py", "--url", url, "--username", username, "--password", password,  "mavlink", "--device", mavlink_stream]
	os.execv("interop_cli.py", args)
	exit(0); 

#make sure the execed processes gets exited on ^c 
def signal_handler(signal, frame):
	os.kill(mp_pid, signal)
	os.kill(ic_pid, signal)
	exit(0)

signal.signal(signal.SIGINT, signal_handler)


client_instance = AsyncClient(url, username, password)
while(True):
	obstacles=client_instance.get_obstacles() 
	
	#for type in obstacles.result(timeout=1):
		#for obstacle in type:
			#print obstacle
	time.sleep(1)




