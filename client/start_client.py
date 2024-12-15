import socket
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.file import read_config, select_encryption

required_parameters = ['IP', 'PORT', 'PASSWORD','SECURITY']
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

def send_mac(client):
    MAC = config["MAC"]
    client.send(MAC.encode())

def start_client():

    client = authentification()
    send_mac(client)

    while True:
        data = input("Data to send to router : ")

        encrypted_message = encryption(data, config["PASSWORD"])
        client.send(encrypted_message.encode())

        encrypted_response = client.recv(1024).decode()
        response = encryption(encrypted_response, config["PASSWORD"])
        print(response)

    client.close()

start_client()
