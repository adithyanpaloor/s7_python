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
            nickname = nickname[index]
            nicknames.remove(nickname)
            break






