#!/usr/bin/python3

#The above line of code is called the shebang basically to set set the envoinment under which the code has to run

#we are importing the socket function.
import socket
import threading

#creating object for the socket function. The address family INET is for IPV4 and Stream for TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname)
port = 4444

ADDR = (host, port)
#Now we will create a binding of the IPv4 and Port
serversocket.bind((host, port))
#serversocket.bind(ADDR) alternative method as bind takes single parameter.

#Now we will set the server listern, also we can define number of connections to accept.
#serversocket.listen(3)


def handle_client(conn, addr):
    pass

def start():
    serversocket.listen()

    while True:
        conn, addr = serversocket.accept()
        #what the above function does is stores the address as add from where the connection is established i.e the client add
        #and also it stores it as an object conn so that we can sent info back to the coneection from client.
        # the addr is actually a tuple which gives the port and ip address from where the connection was established.
        



print("Server is starting.....")
start()
