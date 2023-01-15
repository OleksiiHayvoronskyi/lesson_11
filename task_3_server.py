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
    try:
        conn, addr = server.accept()
    except KeyboardInterrupt:
        server.close()
        break
    else:
        with conn:
            print('Connected with:', addr)
            data = conn.recv(max_size)
            if not data:
                break
            print(f'Client {addr} at', datetime.now(), 'said:', data)

            conn.sendall(b'The number of sent words')
            print('You sent', len(data.split()), 'words')
            print('====================')


