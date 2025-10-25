import socket
c = socket.socket()
c.connect(('localhost',6666))
print("connected with ",c.recv(1080))