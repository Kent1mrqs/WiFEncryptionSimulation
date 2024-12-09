# Wifi Connection Simulation

## Overview

This project simulates a simplified WiFi connection to demonstrate key aspects of network security and cryptographic protocols. 
The goal is to recreate the essential components of a secure WiFi protocol, including :
- **Authentication:** Verifying client and server identities.
- **Key Exchange:** Establishing a shared secret over an insecure channel.
- **Data Encryption:** Ensuring secure communication.
- **Packet Transmission:** Simulating the exchange of encrypted packets.

## Key Features
- **Authentication:** Simulates a pre-shared key (PSK) mechanism, similar to WPA2/3.
- **Key Exchange:** Implements the **Diffie-Hellman** algorithm to securely establish session keys.
- **Data Encryption:** Protects data using a basic encryption method: **XOR**.
- **Packet Transmission:** Models the exchange of encrypted data between an Access Point (AP) and Clients.

## Authentication
Authentication ensures that both the client and server can verify each other's identities before establishing a secure connection.
This is achieved through a Pre-Shared Key (PSK) combined with a Challenge-Response Protocol:

1. The server generates a random challenge and sends it to the client.
2. The client computes a response using the shared PSK and the challenge.
3. The server verifies the response to authenticate the client.

## Key Exchange
### Diffie-helman exchange
Diffie-Hellmann algorithm allows server and client to securely share a secret key in an insecure channel to finally obtain a shared secret key.

#### How it works
1. Choose a large prime number `p` and a base `g`.
2. Server and client generates a private key `private_key`.
3. Server and client calculates their public key : `public_key = g^private_key % p`
4. Server and client gives each other their public key `received_public_key`
5. Server and client calculates the shared secret key : `shared_key = (received_public_key^private_key) % p`
   This shared key will now be used to encrypt and decrypt messages.

## Data Encryption
Data encryption ensures that all communications between the Access Point and the Client are secure and cannot be easily intercepted. This project uses:

Symmetric Encryption: Both parties use the shared key from the Diffie-Hellman exchange to encrypt and decrypt messages.
Encryption Algorithm: A basic XOR-based encryption or a custom implementation of AES (Advanced Encryption Standard).


## Packet Transmission

The project models the secure exchange of encrypted packets between the Access Point and the Client. Each packet includes:

Encrypted Payload: The data encrypted using the session key.
Nonce: A unique value to prevent replay attacks.
Integrity Check: A simple hash or checksum to verify data authenticity.