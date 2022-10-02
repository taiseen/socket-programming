import socket

HOST = '192.168.0.199'
PORT = 50050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

number = 12
client.send(str(number).encode(('utf-8')))

print(client.recv(1024).decode('utf-8'))
print(client.recv(1024).decode('utf-8'))
# print(client.recv(1024).decode('utf-8'))