# Завдання 2. Додайте до сервера з першого завдання функцію чат-боту, який би
# надсилав клієнту задані відповді на певні повідомлення.

from datetime import datetime
import socket


# КЛІЄНТ

print('--- Task 2. TCP Client ---')


address = ('localhost', 53132)
max_size = 1024

print('Client has been started at', datetime.now(), '\n')
name = input(str('Enter your name: '))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Trying to connect to', address)
client.connect(address)

client.sendall(name.encode())
c_name = client.recv(max_size)
c_name = c_name.decode()
print(c_name, 'has joined to the chat room')
print('Enter [break] to exit chat room]\n')

while True:
    message = client.recv(max_size)
    message = message.decode()
    print(c_name, ":", message)
    message = input(str("Me: "))
    if message == 'break':
        message = "Left chat room!"
        client.send(message.encode())
        print("\n")
        break
    client.send(message.encode())




# print('Client has been started at', datetime.now(), '\n')
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(address)
# client.sendall(b'Hey, Server!'.upper())
# data = client.recv(max_size)
# print('At', datetime.now(), 'Server answered:', data)
#
# print('====================')
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(address)
# client.sendall(b'I want to get info, Server!'.upper())
# data = client.recv(max_size)
# print('At', datetime.now(), 'Server answered:', data)

client.close()