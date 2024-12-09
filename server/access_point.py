import socket
import threading
from ap_config import p,g,private_key_ap

def xor_encrypt_decrypt(message, key):
    key = str(key)
    encrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, key * len(message)))
    return encrypted

public_key_ap = (g ** private_key_ap) % p

def start_ap():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)
    print("AP en attente de connexion...")
    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr, private_key_ap, public_key_ap, p))
        client_thread.start()

def handle_client(conn, addr, private_key_ap, public_key_ap, p):
    print(f"Client connecté : {addr}")
    try:
        # Échange de clés Diffie-Hellman
        client_public_key = int(conn.recv(1024).decode())
        conn.send(str(public_key_ap).encode())

        shared_key = (client_public_key ** private_key_ap) % p

        # Réception et déchiffrement des messages
        encrypted_message = conn.recv(1024).decode()
        decrypted_message = xor_encrypt_decrypt(encrypted_message, shared_key)
        print(f"Message déchiffré : {decrypted_message}")

        # Réponse
        response = "Message reçu"
        encrypted_response = xor_encrypt_decrypt(response, shared_key)
        conn.send(encrypted_response.encode())
    except Exception as e:
        print(f"Erreur avec le client {addr}: {e}")
    finally:
        conn.close()

start_ap()
