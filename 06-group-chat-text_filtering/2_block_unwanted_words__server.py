import threading
import socket


#localhost
host = "127.0.0.1"
# do not take any reserved or well known ports
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

filtering_words = ['crime', 'religion', 'politics','terrorist']


#broadcasting messages from the server to all the clients
def broadcast(message):
    #implement the filtering of the messages here
    #implement the brand analytics and tracking here

    for client in clients:
        client.send(message)


def filtering_words_system(clint_input_text):

    input_word_list = clint_input_text.split()

    for input_word in range(len(input_word_list)):

        for filter_word in range(len(filtering_words)):

            if input_word_list[input_word] == filtering_words[filter_word]:

                input_word_list[input_word] = '(this is BlockedWord)'

            else:
                continue

    rejoin_valid_words = " ".join(input_word_list)
    block_word_info = bytes(rejoin_valid_words, 'ascii')
    
    return block_word_info



def handle(client):
    while True:
        try:
            #receiving 1024 bytes
            message = client.recv(1024).decode('ascii')

            # 🟡🟡🟡 Custom function call here...
            broadcast(filtering_words_system(message))

        except:
            #find out the index of the failed client frm the clients list
            index = clients.index(client)
            clients.remove(client)
            client.close()

            #we also remove the nickname of the removed client
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode('ascii'))
            nicknames.remove(nickname)
            break



def receive():
    while True:
        print("receive function is running on the server!")
        # returns a tuple
        client,address = server.accept()

        #you have cut down the address str type casting
        print(f"Connected with {str(address)}")

        #we need to ask the client for the nickname
        #made change here
        name = "NICK"
        client.send(name.encode('ascii'))

        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")

        broadcast(f"{nickname} joined the chat".encode('ascii'))
        #letting know the specific client that it has connected to the server
        client.send("Connected to the server".encode('ascii'))

        #define and run a thread
        #because we want to be able to handle multi clients same time

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()



#main method
print("Server is running ✅✅✅")
receive()