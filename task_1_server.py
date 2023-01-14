# Завдання 1. Реалізувати чат без графічного інтерфейсу для обміну
# повідомленнями між клієнтом та сервером. Клієнт повинен отримувати
# повідомлення сервера.

from datetime import datetime
import socket

# СЕРВЕР

print('--- Task 1. TCP Server ---')

address = ('localhost', 6000)
max_size = 1024

print('Server has been started at', datetime.now())
print('Server is waiting on a client...')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

conn, addr = server.accept()
print('Connected with:', addr)
data = conn.recv(max_size)
print(f'Client {addr} said:', data)
print('At', datetime.now(), conn, 'said', data)
conn.sendall(b'Do you want to talk with me?'.upper())

print('====================')

conn, addr = server.accept()
print('Talking with:', addr)
data = conn.recv(max_size)
print(f'Client {addr} at', datetime.now(), 'said:', data)
conn.sendall(b'How can I help you?'.upper())


conn.close()
server.close()
