#!/usr/bin/env python

import socket
import keyboard

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "localhost"
PORT = 9939
client.connect((IP, PORT))

kembali = 0

def mengirimPesan(message):
    pesan = message
    pesan.encode('utf-8')
    client.send(pesan)
    print("pesan" + pesan + "terkirim")

def keyboard_listening():
    if keyboard.is_pressed('a'):
        mengirimPesan("maju")
        print("A is presseed")
    elif keyboard.is_pressed('s'):
        mengirimPesan("mundur")
        print("S is pressed")
    elif keyboard.is_pressed('x'):
        global kembali
        kembali = 1

if __name__ == '__main__':
    while True:
        try:
            print("tekan a maju")
            print("tekan s mundur")
            keyboard_listening()
            if kembali == 1:
                break
        except:
            break