import socket

s = socket.socket()
print("socket created")
s.bind(('localhost',5656))
s.listen(3)
print("server is running, waiting for connection")

while True:
    c,addr = s.accept()
    print("connected with ",addr," " ,c)
    c.send(bytes('you connected Adithyans server','utf-8'))
    print(c.recv(1024))
    c.close()
