
import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "!Disconnect"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode('utf-8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}] {msg}")
            msg = input("server:")
            conn.send(msg.encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active Connections] {threading.activeCount() -1}")

print("[STARTING] server is starting...")
start()
