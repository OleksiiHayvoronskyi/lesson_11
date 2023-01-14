# Завдання 2. Додайте до сервера з першого завдання функцію чат-боту, який би
# надсилав клієнту задані відповді на певні повідомлення.

from datetime import datetime
import socket


# КЛІЄНТ

print('--- Task 2. TCP Client ---')


address = ('localhost', 6000)
max_size = 1024

print('Client has been started at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'Hey, Server!'.upper())
data = client.recv(max_size)
print('At', datetime.now(), 'Server answered:', data)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'I want to get info, Server!'.upper())
data = client.recv(max_size)
print('At', datetime.now(), 'Server answered:', data)

client.close()