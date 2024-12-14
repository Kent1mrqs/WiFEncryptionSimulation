import socket
from client_config import p,g,private_key_client
from utils import rc4, read_config

public_key_client = (g ** private_key_client) % p
public_key_client_str= str(public_key_client)

def connect_to_server(client):
    config = read_config("wifi_config.txt")

    if 'IP' not in config or 'PORT' not in config or 'MAC' not in config:
        print("IP, MAC or PORT not found in configuration file. Please update 'wifi_config.txt'.")
        return

    client.connect((config['IP'], int(config['PORT'])))
    return client

def diffy_hellmann_exchange(client):
    public_key_client_encoded = public_key_client_str.encode() # The public key needs to be encoded
    client.send(public_key_client_encoded)
    ap_public_key = int(client.recv(1024).decode()) # Client receive servers public key

    shared_key = (ap_public_key ** private_key_client) % p

    print(f"Clé partagée avec l'AP : {shared_key}")
    return shared_key


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 1. Authentification
    client = connect_to_server(client) # Client will now try to connect to server

    # 2. Key Exchange
    shared_key = diffy_hellmann_exchange(client)
    while True:
        #3. Data
        message = input("message ? \n")

        #4. Data Encryption
        encrypted_message = rc4(message, shared_key)
        client.send(encrypted_message.encode())

        encrypted_response = client.recv(1024).decode()
        response = rc4(encrypted_response, shared_key)
        print(response)

    client.close()

start_client()
