# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        #
        ct = data.decode().split(",")
        ct1, ct2 = int(ct[0]), int(ct[1])
        if len(ct) != None:
            print(type(ct1), int(ct2))
        #
        conn.sendall(data)
