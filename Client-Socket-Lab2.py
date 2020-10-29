#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverip = '192.168.176.142'
port = 4444
HEADER = 64
FORMAT = 'utf-8'

clientsocket.connect((serverip, port))

#Now we will define function to sent some message to the server
def send(mesg):
    message = mesg.encode(FORMAT)
    mesg_len = len(message)
    send_len

