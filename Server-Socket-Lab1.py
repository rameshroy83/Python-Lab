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
#serversocket.bind((host, port))

serversocket.bind(ADDR)

#We are defining different functions for Server, Client handling.
#Now we will set the server listern, also we can define number of connections to accept.
#serversocket.listen(3)


# This function is for server handling.
def start():
    serversocket.listen()
    # Once the socket is binded we are making the server to listen for connection request.

    while True:
        conn, addr = serversocket.accept()
        #what the above function does is stores the address as add from where the connection is established i.e the client add
        #and also it stores it as an object conn so that we can sent info back to the coneection from client.
        # the addr is actually a tuple which gives the port and ip address from where the connection was established.
        
        #Now here the purpose of thread is to count the number of active connections.
        #Each client handling would be done as a seperate thread.
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active Connections = {threading.activeCount() - 1}")


def handle_client(conn, addr):
    #This function would run for each client
    print(f"New Connection = {addr} connected")

    connected = True

    while connected:




print("Server is starting.....")
start()
