import socket
import threading

nickname = input("Choose your nickname: ")

# Server IP and port

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1' , 55555))

# Receive function

def receive():
    while True:
        try:
            # Receive message from server
            # If 'NICK' send nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close connection when error
            print("An error occured!")
            client.close()
            break

# Write function

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

# Threads for listening and writing


receive_thread = threading.Thread(target=receive)
receive_thread.start()
