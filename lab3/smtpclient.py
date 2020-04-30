from socket import *



msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"



# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.example.com", 25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
print("Connecting...")
clientSocket.connect(mailserver)


#Confirm connection
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')
	#clientSocket.close()
	#sys.exit()


# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')
	#clientSocket.close()
	#sys.exit()

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM:<example@email.com>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
	print('250 reply not recieved from server.')
	#clientSocket.close()
	#sys.exit()

# Send RCPT TO command and print server response. 
rcptTo = "RCPT TO:<example@email.com>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
	print('250 reply not recieved from server.')
	#clientSocket.close()
	#sys.exit()

# Send DATA command and print server response. 
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
	print('354 reply not recieved from server.')
	#clientSocket.close()
	#sys.exit()

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
	print('250 reply not recieved from server.')
	#clientSocket.close()
	#sys.exit()

# Send QUIT command and get server response.
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
	print('221 reply not recieved from server.')
	#clientSocket.close()
	#sys.exit()

#Close socket
clientSocket.close()
