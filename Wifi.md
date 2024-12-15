# Wifi 

## Overview

1. [Discover Available Networks](#discover-available-networks)
2. [Select a Network](#select-a-network)
3. [Authentification](#authentification)
4. [IP Address Assignement](#ip-address-assignement)
5. [Establish a Connection](#establish-a-connection)
6. [Security Handshake](#security-handshake)
7. [Information Communication](#information-communication)


## Discover Available Networks
- The device scans for nearby Wi-Fi networks.
- The device lists networks within range and showing their names (SSIDs).
- User chooses the network he wants to connect to from the list of available networks. 
- If the network is hidden, User needs to manually enter the SSID.
## Authentification
- Open Network: No password is required; you connect immediately.
- Secured Network: You need to enter a password or use other authentication methods such as:
  - WEP: Now considered as vulnerable. See [documentation](encryption/WEP/README.md).
  - WPA/WPA2 Password: Common in most home and office networks.
  - WPA3: More secure modern standard.
  - Enterprise Authentication: Requires credentials like a username and password or a certificate.
## IP Address Assignement
- Once authenticated, your device communicates with the router to obtain an IP address.
- This is typically done through DHCP (Dynamic Host Configuration Protocol).
- If the network uses static IPs, you must manually configure the IP address, gateway, and DNS settings.

## Establish a Connection
- The device and router exchange packets to establish a stable connection.
- The router confirms access, and your device joins the network.
## Security Handshake
- For secured networks, encryption protocols (like WPA2 or WPA3) initiate a handshake to establish a secure connection.
- Data sent between your device and the router is encrypted to prevent eavesdropping.
## Information Communication 
- The device verifies the connection by sending test packets to the internet (e.g., pinging a server).
- If successful, the device declares the connection active and ready for internet or local network use.