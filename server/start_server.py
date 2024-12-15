import socket
import threading
import time
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.file import read_config, select_encryption

required_parameters = ['PORT', 'PASSWORD']
config = read_config("wifi_config.txt", required_parameters)
security = config["SECURITY"]
encryption = select_encryption[security]


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', int(config["PORT"])))
    server.listen(3)
    print("AP en attente de connexion...")
    while True:
        connection, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(connection, addr))
        client_thread.start()

def generate_challenge():
    timestamp = int(time.time() * 1e9)
    challenge = str(timestamp)
    return challenge

def authentification(connection):
    challenge = generate_challenge()

    connection.send(challenge.encode())
    client_decrypted_challenge = connection.recv(1024).decode()

    encrypted_password = encryption(challenge, config["PASSWORD"])

    if encrypted_password == client_decrypted_challenge:
        connection.send("Connection successful.".encode())
        print("Client successfully connected")
    else:
        connection.send("AUTH_FAILED".encode())
        print("Connection Tentative failed. Wrong Password.")
        connection.close()

def handle_client(connection, addr):
    print(f"Start Connection : {addr}")
    try:
        authentification(connection)

        while True:
            encrypted_message = connection.recv(1024).decode()
            decrypted_message = encryption(encrypted_message, config["PASSWORD"])
            print(f"{addr} sends {decrypted_message}")

            response = "Message received"
            encrypted_response = encryption(response, config["PASSWORD"])
            connection.send(encrypted_response.encode())

    except Exception as e:
        print(f"Erreur avec le client {addr}: {e}")
    finally:
        print(f"End Connection : {addr}")
        connection.close()

start_server()
