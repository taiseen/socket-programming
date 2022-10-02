import socket

HOST = '192.168.0.199'
PORT = 9090

# client object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket = Host + Port
client.connect((HOST, PORT))

client.send('\nHello Server.......... '
            '\nHow are you? 😎'
            '\nTel me something about you... 🧐'
            .encode('utf-8'))

message = client.recv(1024).decode('utf-8')

print(f'Message received from server : {message}')

# Your using port become free...
# to use by other program...
client.close()