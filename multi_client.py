import socket
import threading

# Create client socket and connect
c = socket.socket()
c.connect(('localhost', 6060))

username = input("Enter username: ")

# Function to continuously receive messages
def receive():
    while True:
        try:
            message = c.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                c.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("Disconnected from server.")
            c.close()
            break

# Function to continuously send messages
def write():
    while True:
        msg = input('')
        message = f"{username}: {msg}"
        c.send(message.encode('utf-8'))

# Start threads for sending and receiving
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
