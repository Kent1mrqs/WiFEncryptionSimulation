# Wifi Connection Simulation

## Project Description
For my RTU cryptography class, I choose this topic in order to put pratical application to cryptography algorithm. In this project I will use Diffie-hellman protocol and different encryption algorithm, you can find more information in the documentation.


## Overview

This project simulates a simplified WiFi connection to demonstrate key aspects of network security and cryptographic protocols. 
The goal is to recreate the essential components of a secure WiFi protocol, including :
- **Authentication:** Verifying client and server identities.
- **Key Exchange:** Establishing a shared secret over an insecure channel.
- **Data Encryption:** Ensuring secure communication.
- **Packet Transmission:** Simulating the exchange of encrypted packets.

## Wifi Key Features
> What are the steps of a WiFi connection between a WiFi device trying to connect to a WiFi Router ?
- **Discover Available Networks:** Device will try to find WiFi SSIDs in proximities for User to connect.
- **Authentification:** Then Device will try to 
- **IP Address Assignement:**
- **Establish a Connection:**
- **Security Handshake:**
- **Information Communication:**


For more details, check the [documentation](Network/Wifi.md). 

## Simulation Key Features
> Here are the steps of the simulation of simplified WiFi Connection :
- **Authentication:** Simulates a pre-shared key (PSK) mechanism, similar to WPA2/3.
- **Key Exchange:** Implements the **Diffie-Hellman** algorithm to securely establish session keys.
- **Data Encryption:** Protects data using a basic encryption method: **XOR**.
- **Packet Transmission:** Models the exchange of encrypted data between an Access Point (AP) and Clients.

For more details, check the [documentation](Simulation.md). 


## How to use

### Server / Router
- Open a terminal
- Clone server repository 
- Open [`wifi_config.txt`](server/wifi_config.txt) and complete it with wanted parameters.
- Then start the server with `python3 start_server.py`

### Client / Device
- Open a new terminal
- Clone client repository 
- Open [`wifi_config.txt`](client/wifi_config.txt)
- Enter the parameters of you server..
- Then start the client with `python3 start_client.py`
- You can simulate several connections if you restart these steps.


## Potential Improvements
### Network
#### Client connects to Server
- SSID Broadcast : Server sends its SSID name to port 3636 for a client to connect to it
- Server Discovery : Client listens on 3636, and choose SSID.
- Association request : Client send an association request to server
- IP Attribution (Static IP / DHCP ) 
#### Client communicates with Network
- ARP table and arp request
- Broadcasting and routing

### Cryptography
- WPA1/2/3
- Add a schema of the authentification handshake
- crc-32 integrity checksum
### Pentesting
- Hack WEP network simulation ? 