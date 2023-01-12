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
print('Server is waiting on a client')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

client, addr = server.accept()
data = client.recv(max_size)
print('At', datetime.now(), client, 'said', data)
client.sendall(b'Do you want to talk with me?')

client.close()
server.close()

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('', 55000))
# sock.listen(5)
# print('Server is running... [push ctrl+C to stop]')
# while True:
#     conn, addr = sock.accept()
#     print('connected:', addr)
#     data = conn.recv(1024)
#     print(str(data))
#     conn.send(data.upper())
#
# conn.close()