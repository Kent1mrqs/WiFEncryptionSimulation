import socket
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.file import read_config, select_encryption, generate_iv

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
        iv_response = generate_iv()
        encrypted_message = encryption(data, config["PASSWORD"] + str(iv_response))
        iv_response_bytes = bytes(iv_response)
        encrypted_message_bytes = encrypted_message.encode('utf-8')

        message_to_send = iv_response_bytes + encrypted_message_bytes
        connection.send(message_to_send)

        response = connection.recv(1024)
        iv = response[:3]
        encrypted_response = response[3:].decode('utf-8')
        response = encryption(encrypted_response, config["PASSWORD"] + str(iv))

        print(response)

    connection.close()

start_client()
