import threading
import socket
import matplotlib.pyplot as plt   # pip install matplotlib
import numpy as np


# localhost
host = "127.0.0.1"
# do not take any reserved or well known ports
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

a = []
b = []

brandName = {'BMW': 0, 'Toyota': 0, '7up': 0, 'Hero': 0, 'Honda': 0, 'Samsung': 0}


# text filtering system
def brand_name_counter(sms):

    message = str(sms)
    wordList = message.split()

    # loop at user inputs...
    for word in wordList:

        # loop at our word collections...
        for brand in brandName:

            # check user input word are present in our word collection...
            if brand.lower() in word.lower():

                # increment that brand name count value
                brandName[brand] += 1

                # set value for bar chat display
                a.append(brandName[brand])
                b.append(brand)


# data represent at bar chat 
def bar_chat_data_display():
    x = np.array(b)
    y = np.array(a)
    plt.bar(x, y)
    plt.show()
    print(brandName)


# broadcasting messages from the server to all the clients
def broadcast(message):
    # implement the filtering of the messages here
    # implement the brand analytics and tracking here

    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            # receiving 1024 bytes
            message = client.recv(1024)

            # 🟡🟡🟡 Custom function call here...
            brand_name_counter(message)

            broadcast(message)

        except:
            # find out the index of the failed client frm the clients list
            index = clients.index(client)
            clients.remove(client)
            client.close()
            # we also remove the nickname of the removed client
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode('ascii'))
            nicknames.remove(nickname)

            print(brandName)
            
            # 🟡🟡🟡 Custom function call here...
            bar_chat_data_display()
            break


def receive():
    while True:
        print("receive function is running on the server!")
        # returns a tuple
        client, address = server.accept()

        # you have cut down the address str type casting
        print(f"Connected with {str(address)}")

        # we need to ask the client for the nickname
        # made change here
        name = "NICK"
        client.send(name.encode('ascii'))

        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")

        broadcast(f"{nickname} joined the chat".encode('ascii'))
        # letting know the specific client that it has connected to the server
        client.send("Connected to the server".encode('ascii'))

        # define and run a thread
        # because we want to be able to handle multi clients same time

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# main method
print("Server is running ✅✅✅")
receive()