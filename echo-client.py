import socket

HOST = '127.0.0.1'
PORT = 8100

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = input().encode('utf-8')
        s.sendall(data)
        rec = s.recv(1024)
        print('Received', repr(rec))
        # rec = s.recv(1024)
        # print()
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))