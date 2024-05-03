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
        ct1, ct2 = ct[0], ct[1]
        t = (ct1, ct2)

        if len(ct) != None:
            print(t)
        #
        conn.sendall(data)
