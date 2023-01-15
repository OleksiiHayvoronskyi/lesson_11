# Завдання 2. Додайте до сервера з першого завдання функцію чат-боту, який би
# надсилав клієнту задані відповді на певні повідомлення.

from datetime import datetime
import socket

# СЕРВЕР

print('--- Task 2. TCP Server ---')

address = ('localhost', 53132)
max_size = 1024

print('Server has been started at', datetime.now())
print('Server is waiting on a client...\n')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

while True:
    conn, addr = server.accept()
    with conn:
        print('Connected with:', addr)
        data = str(conn.recv(max_size), encoding='utf_8')
        if not data:
            break
        print(f'Client {addr} said:', data)
        # Повідомлення сервера.
        server_message = data
        print('====================')
        conn.sendall(server_message.encode())
        conn.close()

