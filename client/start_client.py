import socket
from utils import rc4, read_config

def connect_to_server(client):
    config = read_config("wifi_config.txt")

  #  if any(['IP','PORT','MAC','PASSWORD'] not in config):
  #      print("IP, MAC, PORT or PASSWORD not found in configuration file. Please update 'wifi_config.txt'.")
  #      return

    client.connect((config['IP'], int(config['PORT'])))
    return client

def start_client():
    config = read_config("wifi_config.txt")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 1. Authentification
    client = connect_to_server(client) # Client will now try to connect to server

    challenge = client.recv(1024).decode()
    print("challenge :", challenge)
    # 2. Key Exchange
    decrypted_challenge = rc4(challenge,config["PASSWORD"] )
    client.send(decrypted_challenge.encode())

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
