import socket
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.file import read_config, select_encryption

required_parameters = ['IP', 'PORT', 'MAC', 'PASSWORD','SECURITY']
config = read_config("wifi_config.txt", required_parameters)
security = config["SECURITY"]
encryption = select_encryption[security]

def authentification():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((config['IP'], int(config['PORT'])))

    challenge = client.recv(1024).decode()
    decrypted_challenge = encryption(challenge,config["PASSWORD"] )
    client.send(decrypted_challenge.encode())

    auth_response = client.recv(1024).decode()
    if auth_response == "AUTH_FAILED":
        print("Wrong password.")
        client.close()
        return
    else:
        print("Successfully connected")

    return client

def start_client():

    client = authentification()

    while True:
        message = input("message ? \n")

        encrypted_message = encryption(message, config["PASSWORD"])
        client.send(encrypted_message.encode())

        encrypted_response = client.recv(1024).decode()
        response = encryption(encrypted_response, config["PASSWORD"])
        print(response)

    client.close()

start_client()
