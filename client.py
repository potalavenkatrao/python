import socket # for socket
import sys

try:
    s = socket.socket()
    print(socket.AF_INET,socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

port=12345

try:
    host_ip = socket.gethostbyname("localhost")
except socket.gaierror:
	print("there was an error resolving the host")
	sys.exit()

# connecting to the server
s.connect((host_ip, port))
s.send('Roses are red'.encode())
print (s.recv(1024).decode())

print ("the socket has successfully connected to ",host_ip)