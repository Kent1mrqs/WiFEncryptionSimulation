import socket
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.rc4 import rc4
from utils.file import read_config

required_parameters = ['IP', 'PORT', 'MAC', 'PASSWORD']
config = read_config("wifi_config.txt", required_parameters)

def connect_to_server(client):

    client.connect((config['IP'], int(config['PORT'])))
    return client

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 1. Authentification
    client = connect_to_server(client) # Client will now try to connect to server
    challenge = client.recv(1024).decode()

    # 2. Key Exchange
    decrypted_challenge = rc4(challenge,config["PASSWORD"] )
    client.send(decrypted_challenge.encode())

    auth_response = client.recv(1024).decode()
    if auth_response == "AUTH_FAILED":
        print("Wrong password.")
        client.close()
        return
    else:
        print("Successfully connected")

    while True:
        #3. Data
        message = input("message ? \n")

        #4. Data Encryption
        encrypted_message = rc4(message, config["PASSWORD"])
        client.send(encrypted_message.encode())

        encrypted_response = client.recv(1024).decode()
        response = rc4(encrypted_response, config["PASSWORD"])
        print(response)

    client.close()

start_client()
