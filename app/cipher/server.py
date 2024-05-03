# Echo server program
import socket
import pickle 
from time import sleep
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port


def receive(s, conn, addr):
    
    with conn:
        print('Connected by', addr)
        while True:
            #sleep(3)
            data = conn.recv(1024)
            if not data:
                break
            received_obj = pickle.loads(data)
            print('Received:', received_obj)
            return received_obj
