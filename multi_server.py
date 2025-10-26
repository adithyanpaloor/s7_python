import socket
import threading

# Create socket
s = socket.socket()
s.bind(('localhost', 6060))
s.listen(5)
print("Server is listening...")

clients = []
usernames = []

# Broadcast message to all connected clients
def broadcast(message, _client=None):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                pass  # if client already disconnected

# Handle messages from a single client
def handle_clients(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                username = usernames[index]
                broadcast(f"{username} left the chat.".encode('utf-8'))
                usernames.remove(username)
                client.close()
            break

# Accept and handle new connections
def receive_connections():
    while True:
        client, address = s.accept()
        print('Connected with', address)

        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        print(f"Username is {username}")
        broadcast(f"{username} joined the chat.".encode('utf-8'))
        client.send("Connected to the chat!".encode('utf-8'))

        thread = threading.Thread(target=handle_clients, args=(client,))
        thread.start()

# Start server
receive_connections()

