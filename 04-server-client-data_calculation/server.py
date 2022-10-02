import socket

HOST = '192.168.0.199'
PORT = 50050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

ticket_id = 100
totalHit = 0

print('🟩🟩🟩 Connection Start...')

while True:
    communication_socket, address = server.accept()

    data = communication_socket.recv(1024).decode('utf-8')
    message = int(data)
    
    print(f'Client send ==> {message}')
    communication_socket.send(f"Your ticket ID is : {ticket_id}".encode('utf-8'))

    if message > 10:
        communication_socket.send(f"Number is bigger then 10\n".encode('utf-8'))
    else:
        communication_socket.send(f"Number is smaller then 10\n".encode('utf-8'))

    list = []
    for i in range(1, message):
        if message % i == 0:
            list.append(i)


    communication_socket.send(f"Your given number is divide by this : {list}".encode('utf-8'))


    ticket_id = ticket_id + 1
    totalHit = totalHit + 1
    print(f"Total number of hits : {totalHit}")

    communication_socket.close()
    print(f"🟥🟥🟥 Connection End with {address}")