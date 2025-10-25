import socket
s = socket.socket()
s.bind(('localhost',6222))
s.listen(4)
print("server is listening")
while True:
    c,aadr = s.accept()
    print('server is connected with ',c)
    c.send(bytes('server3','utf-8'))
    print(c.recv(1024))
    c.close()
 