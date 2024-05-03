# Echo client program
import socket
from elGamal import ElGamal as eg
from Cryptodome.Random import random
import pickle
HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server

ciph = eg()
ciph.setPK(pow(ciph.g, random.randrange(1,ciph.p - 1), ciph.p))
ctVector = ciph.vector(5)

def send(data, h):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((h, PORT))
        s.sendall(pickle.dumps(data))
        data = s.recv(1024)
    print('Received', repr(data))

send(ctVector, "127.0.0.1") # ip address of server
send(51293702193, "127.0.0.1")