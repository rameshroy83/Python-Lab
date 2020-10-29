#!/usr/bin/python3

#The above line of code is called the shebang basically to set set the envoinment under which the code has to run

#we are importing the socket function.
import socket
import threading

# Defining Variables
host = '192.168.176.142'
port = 4444
ADDR = ('192.168.176.142', port)
FORMAT = 'utf-8'
HEADER = 64
Disconnect_message = '!Disconnect'


#creating object for the socket function. The address family INET is for IPV4 and Stream for TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Now we will create a binding of the IPv4 and Port
#serversocket.bind((host, port))
serversocket.bind(ADDR)

#Now we will set the server listern, also we can define number of connections to accept.
#serversocket.listen(3)

# We are defining various functions for Server and Client.
#Following is the server function, where we will start the server to listen.
def start():
    serversocket.listen()
    print(f"Server has started----------")
    #We will print the server port where the Server is listerning:
    print(f"The Server {host} is listenting at port{port}")
    while True:
        conn, addr = serversocket.accept()
        #what the above function does is stores the address as add from where the connection is established i.e the client add
        #and also it stores it as an object conn so that we can sent info back to the coneection from client.
        # the addr is actually a tuple which gives the port and ip address from where the connection was established.

       

       #Now we will create thread so that we can print connection from each client.
        thread = threading.Thread(target=handle_client, args=(conn, addr))
       # There would be seperate thread for each client connection, and we will define the thred details
       # under the handle_client function. Now that we have created the thread, we will print the new incoming
       # connnection.
        thread.start()
        print(f"Total Active connections is {threading.activeCount() - 1}")


# This function is defining how client connection is being handled.
def handle_client(conn, addr):
    print(f"New Client Connection came from {addr}")

    connected = True
    while connected:
        mesg_len = conn.recv(HEADER).decode(FORMAT)
        if mesg_len:
            mesg_len = int(mesg_len)
            mesg = conn.recv(mesg_len).decode(FORMAT)
            print(f"{addr} : {mesg}")
            if mesg == Disconnect_message:
                connected = False
    conn.close()
    # In the above code we are defining HEADER and FORMAT, which is basically to set the length of the packet
    #size allowed from the client and decoding the information.
    #We are also reading if any disconnection request is receive if so we are marking the connected
    #state to False and closing the connection.


start()
