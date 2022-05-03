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
    nerima = client.recv(1034).decode('utf-8')
    print(nerima)
    if nerima == 'berhenti':
        selesai = True
    if nerima == 'hello':
        print('hello terdeteksi', nerima)
    else:
        print(nerima)
    pesan = raw_input("pesan yang akan dikirim: ").encode('utf-8')
    client.send(pesan)

