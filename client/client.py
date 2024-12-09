import socket
from client_config import p,g,private_key_client
from utils import xor_encrypt_decrypt, simulate_wifi_connection

public_key_client = (g ** private_key_client) % p

def start_client():
    simulate_wifi_connection()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    # Échange de clés Diffie-Hellman
    client.send(str(public_key_client).encode())
    ap_public_key = int(client.recv(1024).decode())

    shared_key = (ap_public_key ** private_key_client) % p
    print(f"Clé partagée avec l'AP : {shared_key}")

    # Envoi d'un message chiffré
    message = "Hello, AP!"
    encrypted_message = xor_encrypt_decrypt(message, shared_key)
    print(f"Message chiffré envoyé : {encrypted_message}")
    client.send(encrypted_message.encode())

    # Réception de la réponse
    encrypted_response = client.recv(1024).decode()
    response = xor_encrypt_decrypt(encrypted_response, shared_key)
    print(f"Réponse déchiffrée : {response}")

    client.close()

start_client()
