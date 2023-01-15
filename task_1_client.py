# Завдання 1. Реалізувати чат без графічного інтерфейсу для обміну
# повідомленнями між клієнтом та сервером. Клієнт повинен отримувати
# повідомлення сервера.

from datetime import datetime
import socket


# КЛІЄНТ

print('--- Task 1. TCP Client ---')

address = ('localhost', 60000)
max_size = 1024

print('Client has been started at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'Hey, Server!'.upper())
data = client.recv(max_size)
print('Server at', datetime.now(), 'answered', data)

client.close()
