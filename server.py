#!/usr/bin/env python

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "localhost"
PORT = 9999
server.bind((IP,PORT))

server.listen(4)
client, addr = server.accept()

selesai = False

while not selesai:
    nerima = client.recv(1034)
    nerima.decode('utf-8')
    if nerima == "berheni":
        selesai = True
    else:
        print(nerima)
    # pesan = input("pesan yang akan dikirim: ")
    # cobasaja = pesan + str.encode('utf-8')
    client.send(input("masukkan pesan: ").encode('utf-8'))

