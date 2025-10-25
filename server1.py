import socket
s = socket.socket()
print("socket created")
s.bind(('localhost',5555))
s.listen(4)
print("server is listening")

while True:
    c,addr = s.accept()
    print('server connected with :' , addr)
    c.send(bytes('good morning ','utf-8' ))
    c.close()

