# Завдання 3. Напишіть сервер, який би отримував у користувача фразу, а потім
# надсилав би підраховану кількість слів у відповідь.


from datetime import datetime
import socket

# СЕРВЕР

print('--- Task 3. TCP Server ---')


address = ('localhost', 63201)
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
        data = conn.recv(max_size)
        if not data:
            break
        print(f'Client {addr} said:', data)
        #print(conn.sendall(b'I counted the number of written words'))
        #print('You said', len(data.split()), 'words')
        # Рахує кількість слів у рядку.
        #print('You said', len(data.split()),'words')
        # print('At', datetime.now(), conn, 'said', data)

        conn.sendall(b'I counted the number of written words')
        print('You said', len(data.split()), 'words')
        print('====================')

