import socket
import threading
from ap_config import p,g,private_key_ap
from utils import rc4


public_key_ap = (g ** private_key_ap) % p

def start_ap():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(3)
    print("AP en attente de connexion...")
    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr, private_key_ap, public_key_ap, p))
        client_thread.start()

def handle_client(conn, addr, private_key_ap, public_key_ap, p):
    print(f"Client connected : {addr}")
    try:
        client_public_key = int(conn.recv(1024).decode())
        conn.send(str(public_key_ap).encode())

        shared_key = (client_public_key ** private_key_ap) % p

        while True:

            encrypted_message = conn.recv(1024).decode()
            decrypted_message = rc4(encrypted_message, shared_key)
            print(f"{addr} sends {decrypted_message}")


            response = "Message received"
            encrypted_response = rc4(response, shared_key)
            conn.send(encrypted_response.encode())

    except Exception as e:
        print(f"Erreur avec le client {addr}: {e}")
    finally:
        print(f"Client disconnected : {addr}")
        conn.close()

start_ap()
