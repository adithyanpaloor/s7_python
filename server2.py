import socket
s = socket.socket()
print("socket created")
s.bind(('localhost',6666))
s.listen()
print(" server is listening..... ")
while True:
    c, addr = s.accept()
    print("sever is connected with - ",c)
    c.send(bytes('server 2','utf-8'))
    c.close()
