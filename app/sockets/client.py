<<<<<<< Updated upstream
# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
f = open("msg.txt", "r")
msg = f.readline()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(msg, encoding="utf-8"))
    data = s.recv(1024)
=======
# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
f = open("msg.txt", "r")
msg = f.readline()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(msg, encoding="utf-8"))
    data = s.recv(1024)
>>>>>>> Stashed changes
print('Received', repr(data))