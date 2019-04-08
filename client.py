import os
import socket
import threading
import time

def Main():
    host = '127.0.0.1'
    port = 5051

    # Creating a socket
    s = socket.socket()
    s.connect((host,port))
    print("Client-Server System\n")
    s.send("method")
    time.sleep(50)


if __name__ == '__main__':
    Main()