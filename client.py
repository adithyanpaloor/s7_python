import socket
c =  socket.socket()
c.connect(('localhost',5656))
print(c.recv(1024))
msg = input("enter your name: ")

c.send(bytes(msg,'utf-8'))