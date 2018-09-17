# coding: utf-8

import socket



socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('192.168.56.1', 6969))

while True:
        socket.listen(5)
        client, address = socket.accept()
        response = client.recv(255)
        if response != "":
                print response

client.close()
stock.close()

