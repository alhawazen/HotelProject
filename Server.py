import socket
from datetime import *
from firebase import firebase
import time

firebase = firebase.FirebaseApplication("https://hotelsys-da043/firestore/data~2F",None)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.100.7'
port = 1234
s.bind((host, port))
s.listen(5)
clientSocket, address = s.accept()

print("Connection established")

while True:
    datarec = clientSocket.recv(1024)
