#!/usr/bin/python3

#The above line of code is called the shebang basically to set set the envoinment under which the code has to run

#we are importing the socket function.
import socket

#creating object for the socket function. The address family INET is for IPV4 and Stream for TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

#Now we will create a binding of the IPv4 and Port
serversocket.bind(host, port)

#Now we will set the server listern, also we can define number of connections to accept.
serversocket.listen(3)

