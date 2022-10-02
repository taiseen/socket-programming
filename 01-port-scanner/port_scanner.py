import socket
import threading
from queue import Queue

# putting the default getaway or the localhost
target = "127.0.0.1"


def port_scanner(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        print('could connect')
        return True

    except:
        return False

# print(port_scanner(80))


# for checking a range of ports
# these are all reserved ports so you will not be able to access these ports
for port in range(9087, 9095):
    result = port_scanner(port)
    print(result)
    if result == True:
        print("Port {} is open".format(port))

    else:
        print("Port {} is closed".format(port))


# second approach using threading and queue
# we introduce multithreading to make the scanning process faster,
# we can use queues to make it faster instead,
# we will be queueing the port numbers

queue = Queue()
open_ports = []


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if port_scanner(port):
            print("Port {} is open".format(port))
            open_ports.append(port)

        # you could also give an else statement here


port_list = range(1, 1024)

fill_queue(port_list)

thread_list = []

for i in range(10):
    # we are referring to the worker function without calling it
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)
