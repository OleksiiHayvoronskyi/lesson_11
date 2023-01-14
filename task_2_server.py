# Завдання 2. Додайте до сервера з першого завдання функцію чат-боту, який би
# надсилав клієнту задані відповді на певні повідомлення.

from datetime import datetime
import socket

# СЕРВЕР

print('--- Task 2. TCP Server ---')

address = ('localhost', 6000)
max_size = 1024

print('Server has been started at', datetime.now())
print('Server is waiting on a client...')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)
while True:
    conn, addr = server.accept()
    print('Connected with:', addr)
    data = conn.recv(max_size)
    if not data:
        break
    print(f'Client {addr} said:', data)
    print('At', datetime.now(), conn, 'said', data)
    conn.sendall(b'Do you want to talk with me?'.upper())

    print('====================')