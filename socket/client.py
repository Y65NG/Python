import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6543

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(input().encode())
        data = s.recv(1024)
        print('Received', repr(data))