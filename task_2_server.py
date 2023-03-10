# Завдання 2. Додайте до сервера з першого завдання функцію чат-боту, який би
# надсилав клієнту задані відповді на певні повідомлення.

from datetime import datetime
import socket


# СЕРВЕР

print('--- Task 2. ChatBot ---')

address = ('localhost', 53132)
max_size = 1024

print('Welcome to the ChatBox')
print('Initialising...\n')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
print(address)
name = input(str('Enter your name: '))

server.listen(5)

print("\nWaiting for incoming connections...\n")
conn, addr = server.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, 'has joined to the chat room')
print('Enter [break] to exit chat room]\n')

conn.send(name.encode())

while True:
    message = input(str("Me: "))
    if message == 'break':
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
