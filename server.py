import os
import socket
import threading
import time

global counter

def fileOperation(con, lock):
    global counter
    con.recv(1024)
    if lock.acquire():
        print("Lock Acquired")
        file = open("file.txt", "w+")
        counter +=1
        file.write(str(counter))
        file.close()
        time.sleep(5)
        print("Sleeping 5s")
        lock.release()
        print("Lock Released")


def Main():
    host = '127.0.0.1'
    port = 5051
    # Creating a socket
    global counter
    new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_sock.bind((host, port))
    # Server listening for connections
    new_sock.listen(10)
    lock = threading.Lock()
    print("Server started, waiting for client to accept request...")
    counter = 0
    file = open("file.txt", 'w+')
    file.write(str(counter))
    file.close()
    while True:
        # Get the connection socket
        connection, ip_address = new_sock.accept()
        print("Client connected to ip-address: ")
        print("<", str(ip_address), ">")
        thread = threading.Thread(target=fileOperation, args=(connection,lock))
        # Starting thread
        thread.start()


if __name__ == '__main__':
    Main()