import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5001))
s.sendall("abcde".encode())
d = s.recv(100)
print(d)