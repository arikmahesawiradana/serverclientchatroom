#!/usr/bin/env python

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP = "192.168.244.141"
IP = "localhost"
PORT = 9979
server.bind((IP,PORT))
server.listen(4)
print("server listening.....")
client, addr = server.accept()

def mengirim(message):
    pesan = message
    pesan.encode('utf-8')
    client.send(pesan)

def menerima():
    global nerima
    nerima = client.recv(1034)
    nerima.decode('utf-8')
    print (nerima)

while True:
    menerima()
    mengirim("halo juga")
    menerima()
    mengirim("saya baik kamu?")
    menerima()
    mengirim("berhenti")
    if nerima == 'berhenti':
        break
# selesai = False
#
# while not selesai:
#     nerima = client.recv(1034).decode('utf-8')
#     print(nerima)
#     if nerima == 'berhenti':
#         selesai = True
#     if nerima == 'hello':
#         print('hello terdeteksi', nerima)
#     else:
#         print(nerima)
#     pesan = raw_input("pesan yang akan dikirim: ").encode('utf-8')
#     client.send(pesan)

