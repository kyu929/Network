import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 5001))
s.listen()


c, addr = s.accept()
d = c.recv(100)

print(d)
c.sendall(d[::-1])
