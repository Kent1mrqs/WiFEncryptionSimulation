# Wifi Simulation

## Overview

1. [Authentification](#authentication)
2. [Key Exchange](#key-exchange)
3. [Data Encryption](#data-encryption)
4. [Packet Transmission](#packet-transmission)

## Authentication
Authentication ensures that the client and server can verify each other's identities before establishing a secure connection.
The client will try to connect to the server (ip and port given in client_config.txt).

## Key Exchange
### Diffie-helman exchange
Diffie-Hellmann algorithm allows server and client to securely share a secret key in an insecure channel to finally obtain a shared secret key.

1. Choose a large prime number `p` and a base `g`.
2. Server and client generates a private key `private_key`.
3. Server and client calculates their public key : `public_key = g^private_key % p`
4. Server and client gives each other their public key `received_public_key`
5. Server and client calculates the shared secret key : `shared_key = (received_public_key^private_key) % p`
   This shared key will now be used to encrypt and decrypt messages in [Data Encryption](#data-encryption).

## Data Encryption
Data encryption ensures that all communications between the Access Point and the Client are secure.

Symmetric Encryption: Both parties use the shared key from the [Diffie-Hellman exchange](#diffie-helman-exchange) to encrypt and decrypt messages.
Encryption Algorithm: A basic XOR-based encryption.


## Packet Transmission

The project models the secure exchange of encrypted packets between the Access Point and the Client. Each packet includes:

Encrypted Payload: The data encrypted using the session key.
Nonce: A unique value to prevent replay attacks.
Integrity Check: A simple hash or checksum to verify data authenticity.


## Possible Improvements

- Proper disconnection
- Better encryption
- Authentification challenge