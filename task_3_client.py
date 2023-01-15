# Завдання 3. Напишіть сервер, який би отримував у користувача фразу, а потім
# надсилав би підраховану кількість слів у відповідь.

from datetime import datetime
import socket


# КЛІЄНТ

print('--- Task 3. TCP Client ---')


address = ('localhost', 63201)
max_size = 1024

print('Client has been started at', datetime.now(), '\n')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'Count my words!'.upper())
data = client.recv(max_size)
print('At', datetime.now(), 'Server answered:', data)

print('====================')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'How many words did I send you?'.upper())
data = client.recv(max_size)
print('At', datetime.now(), 'Server answered:', data)
