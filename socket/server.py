import socket

HOST = socket.gethostbyname(socket.gethostname()) 
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024).decode()
            print(data)
            if not data:
                break
            conn.sendall(data.encode())