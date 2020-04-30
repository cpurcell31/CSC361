import socket
import sys


try:
    hostip = sys.argv[1]
    port = sys.argv[2]
    fname = sys.argv[3]
except:
    print("Did not provide enough arguments!")
    print("Please provide ip, port# and file name")
    print("Ex: 127.0.0.1 80 index.html")
    sys.exit(1)

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("Socket Error")
    sys.exit(1)

clientSocket.connect((hostip, int(port)))
clientSocket.send("GET /" + fname + " HTTP/1.1\r\n\r\n")

while True:
    reply = clientSocket.recv(4096)
    if(len(reply) < 1):
	    break
    print(reply)

clientSocket.close()
