import socket
import threading


server = socket.socket()
server.bind(('localhost',8765))
server.listen()

clients = []
nicknames = []

def brodcast(message):
    for client in clients :
        client.send(message)

def hadle(client):
    while True:
        try:
            message = client.recv(1024)
            brodcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            brodcast(f'{client} left the chat '.encode('utf-8'))
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break
def receive():
    while True:
        client,addr = server.accept()
        print(f'connected with {str(addr)}')

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        clients.append(client)
        nicknames.append(nickname)

        print(f'nickname: {nickname}')
        brodcast(f'{nickname} joined the chat '.encode('utf-8'))
        client.send('connected to the server'.encode('utf-8'))

        thread = threading.Thread(target=hadle, args=(client,))
        thread.start()

print("server is listening......")
receive()





