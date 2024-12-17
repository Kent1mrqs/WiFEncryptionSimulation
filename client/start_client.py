import socket
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.file import read_config, select_encryption

required_parameters = ['IP', 'PORT', 'PASSWORD','SECURITY']
config = read_config("client_config.txt", required_parameters)
security = config["SECURITY"]
encryption = select_encryption[security]

def authentification():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((config['IP'], int(config['PORT'])))

    challenge = connection.recv(1024).decode()
    decrypted_challenge = encryption(challenge,config["PASSWORD"] )
    connection.send(decrypted_challenge.encode())

    auth_response = connection.recv(1024).decode()
    if auth_response == "AUTH_FAILED":
        print("Wrong password.")
        connection.close()
        return
    else:
        print("Successfully connected")

    return connection

def start_client():

    connection = authentification()

    while True:
        data = input("Data to send to router : ")

        encrypted_message = encryption(data, config["PASSWORD"])
        connection.send(encrypted_message.encode())

        encrypted_response = connection.recv(1024).decode()
        response = encryption(encrypted_response, config["PASSWORD"])
        print(response)

    connection.close()

start_client()
