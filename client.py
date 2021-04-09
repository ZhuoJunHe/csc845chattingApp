
import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "!Disconnect"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

print("Server connected, please enter your msg to chat with the server. Type '!Disconnect' for disconnect the server \n")
while True:
    msg = input("client:")
    if msg == DISCONNECT_MSG:
        break
    send(msg)

send(DISCONNECT_MSG)
