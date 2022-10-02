import socket

HOST = '192.168.0.199'
PORT = 9090

# server object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket = Host + Port
server.bind((HOST, PORT))

# At a time 5 connection can enter
# max payload
server.listen(5)
print('Server is started...')

while True:

    # 🤝 connection open
    communication_socket, address = server.accept()
    print(f'✅ Connected to : {address}')

    # 👂 listening from client
    message = communication_socket.recv(1024).decode('utf-8')      # 1024 Byte * 8 == ?00000000 bit
    print(f'Message from the client : {message}')

    # 📢 telling to client
    communication_socket.send('\nHello Client.... '
                              '\nHow are you?'
                              '\nI am fine 😊'
                              '\nHop you are fine?'
                              .encode('utf-8'))

    # ❌ connection close
    communication_socket.close()

    print(f'Connected with : {address} has close 🛑')