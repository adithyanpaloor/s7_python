import socket
c = socket.socket()
c.connect(('localhost',5555))
print(c.recv(1080))


