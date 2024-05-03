# Echo client program
import socket
from elGamal import ElGamal as eg
from Cryptodome.Random import random
import pickle
from time import sleep
HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server

ciph = eg()
ciph.setPK(pow(ciph.g, random.randrange(1,ciph.p - 1), ciph.p))
ctVector = ciph.vector(5)

def send(data, s):
    s.sendall(pickle.dumps(data))
    data = s.recv(1024)
    print('Received', repr(data))