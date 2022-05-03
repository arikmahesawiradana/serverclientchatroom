#!/usr/bin/env python

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "localhost"
PORT = 9999
client.connect((IP,PORT))

selesai = False

while not selesai:
    # pesan = input("pesan yang akan dikirim: ")
    # cobasaja = pesan + str.encode('utf-8')
    client.send(input("masukkan pesan: ").encode('utf-8'))
    nerima = client.recv(1034)
    nerima.decode('utf-8')
    if nerima == "berheni":
        selesai = True
    else:
        print(nerima)
