import socket
import sys
import time
import datetime

try:
    hostip = sys.argv[1]
    port = sys.argv[2]
except:
    print("Did not provide enough arguments!")
    print("Please provide ip, port# and file name")
    print("Ex: 127.0.0.1 80 index.html")
    sys.exit(1)

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
    print("Socket Error")
    sys.exit(1)

message = 'ping'
reply = ''
timeStart = 0
timeEnd = 0
timeDif = 0
for x in range(0, 10):
	clientSocket.sendto(message + " " + str(x+1) + " " + str(datetime.datetime.now().time()), (hostip, int(port)))
	timeStart = time.time()
	clientSocket.settimeout(1.0)
	try:		
		reply = clientSocket.recv(1024)
	except:
		continue
	clientSocket.settimeout(None)
	if(reply):
		timeEnd = time.time()
		timeDif = timeEnd - timeStart
		print(reply + " " + str(timeDif*1000) + "ms")


if(len(reply) == 0):
	print("Connection timed out")

clientSocket.close()
