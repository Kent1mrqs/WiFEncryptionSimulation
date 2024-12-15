import socket
import threading
from utils import rc4, read_config

def start_ap():
    config = read_config("wifi_config.txt")

  #  if any(['PORT','PASSWORD'] not in config):
  #      print("PORT or PASSWORD not found in configuration file. Please update 'wifi_config.txt'.")
  #      return

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', int(config["PORT"])))
    server.listen(3)
    print("AP en attente de connexion...")
    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

def generate_challenge():
    return "challenge"

def handle_client(conn, addr):
    config = read_config("wifi_config.txt")
    print(f"Client connected : {addr}")
    try:
        challenge = generate_challenge()
        print("challenge :", challenge)

        conn.send(challenge.encode())
        client_decrypted_challenge = conn.recv(1024).decode()

        encrypted_password = rc4(challenge, config["PASSWORD"])

        if encrypted_password == client_decrypted_challenge:
            print("Client successfully connected")
        else:
            print("Connection Tentative failed. Wrong Password.")
            conn.close()

        while True:
            encrypted_message = conn.recv(1024).decode()
            decrypted_message = rc4(encrypted_message, config["PASSWORD"])
            print(f"{addr} sends {decrypted_message}")

            response = "Message received"
            encrypted_response = rc4(response, config["PASSWORD"])
            conn.send(encrypted_response.encode())

    except Exception as e:
        print(f"Erreur avec le client {addr}: {e}")
    finally:
        print(f"Client disconnected : {addr}")
        conn.close()

start_ap()
