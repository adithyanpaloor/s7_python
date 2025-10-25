import socket
c = socket.socket()
c.connect(('localhost',6222))
print('Connected ', c.recv(1024))
c.send(bytes('hello','uft-8'))