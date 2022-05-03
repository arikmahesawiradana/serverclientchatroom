#!/usr/bin/env python

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pesan = ""

IP = "localhost"
PORT = 9999
client.connect((IP,PORT))

selesai = False

while not selesai:
    pesan = raw_input("masukkan pesan: ").encode('utf-8')
    # cobasaja = str(pesan, encodings='utf-8')
    # pesan = str("hello").encode('utf-8')
    client.send(pesan)
    nerima = client.recv(1034).decode('utf-8')
    print(nerima)
    if nerima == 'berheni':
        selesai = True
    else:
        print(nerima)
