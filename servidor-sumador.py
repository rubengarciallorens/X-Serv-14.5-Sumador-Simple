#!/usr/bin/python


import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

mysocket.bind (('localhost', 1234))

mySocket.listen(4) #Convierto en servidor y digo que solo escuche a 5 clientes como máximo

rndm_num=randome.randint(1,9999999999)

while True:

	print ("Waiting for connections")
	(recvsocket, address)= mySocket.accept()
	print ("HTTP request received:")
	bytes_receive = recvSocket.recv(2048)
	Request = str (bytes_receive, 'utf-8')

	print(Request)	#Veo que me piden
	Resource = Request.split()[1]
	print("Resource: ", Resource)
	_, op1, operacion, op2 = Resource.split('/')
	print(op1, operacion, op2)

	respuesta1= "Procesando: "
	recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + respuesta1, 'utf-8'))
	recvSocket.close()