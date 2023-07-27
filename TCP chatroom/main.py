import threading
import socket

# Server IP and port
host = '127.0.0.1'  # localhost
port = 55555

# Create a TCP socket   
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists for clients and their nicknames

clients = []
nicknames = []

# Broadcast function

def broadcast(message):
    for client in clients:
        client.send(message)

# Handle function

def handle(client):
    while True:
        try:
            # Broadcast messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove and close clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

# Receive function

def receive():
    while True:
        # Accept clients
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request and store nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print and broadcast nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")


receive()

