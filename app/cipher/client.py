# Echo client program
import socket
from Cryptodome.PublicKey import ElGamal as eg

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
f = open("msg.txt", "r")
msg = f.readline()

ciph = eg.eg()
vector = ciph.vector()
ctVector = []
for msg in vector :
    ctVector.append(ciph.encrypt(msg))
    
print(ctVector)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(ctVector, encoding="utf-8"))
    data = s.recv(1024)
print('Received', repr(data))