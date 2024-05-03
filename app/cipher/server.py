# Echo server program
import socket
import pickle 
from time import sleep
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port


def receive(s):
    s.bind((HOST, PORT))
    s.listen(1)
    print("Server started, listening for connections...")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            #sleep(3)
            data = conn.recv(1024)
            if not data:
                break
            received_obj = pickle.loads(data)
            print('Received:', received_obj)
            s.close()
            return received_obj
