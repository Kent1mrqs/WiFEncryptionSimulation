# config.py

# Diffie-Hellman Parameters
p = 23  # Prime number
g = 5   # Générateur

# Clés privées des deux parties (client et AP)
private_key_client = 6  # Clé privée du client
private_key_ap = 15     # Clé privée du point d'accès

# Adresse et port du serveur (AP)
server_address = 'localhost'
server_port = 12345

# Autres configurations, comme le message par défaut à envoyer
default_message = "Hello, AP!"
