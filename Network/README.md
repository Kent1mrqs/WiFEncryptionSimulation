Here’s a simplified version of the README with more accessible language:

---

# Network Documentation

This folder explains how the network part of the WiFi Connection Simulation works. It focuses on how devices communicate, how authentication happens, and how data is sent securely between the client and the server.

## Table of Contents

1. [Introduction](#introduction)
2. [How the Connection Works](#how-the-connection-works)
3. [Protocols Used](#protocols-used)

---

## Introduction

Networks allow devices to talk to each other. In this simulation, we simplify the process of a WiFi connection to focus on key parts:

- Secure communication between a client (device) and a server (router).
- Authentication using a challenge-response method.
- Encrypting data to keep it private during transmission.

The simulation uses TCP, a reliable protocol that ensures all messages are delivered and in the correct order.

---

## How the Connection Works

The connection process between the client and the server has five main steps:

1. **Finding the Server**:
    - The client connects to the server using its IP address and port number.

2. **Authentication**:
    - The server sends a challenge to the client.
    - The client encrypts the challenge using the password and sends it back.
    - If the response is correct, the client is authenticated.

3. **Connection Established**:
    - Once authenticated, the server allows the client to communicate.

4. **Sending Data**:
    - The client sends encrypted data to the server.
    - The server decrypts the data and logs it.

5. **Disconnecting**:
    - Either the client or the server can end the connection.

---

## Protocols Used

This project uses custom rules (protocols) for communication:

- **Authentication Protocol**:  
  Handles the challenge-response process to check the client’s password.

- **Encryption Protocol**:  
  Uses WEP (an older encryption standard) to secure the connection.

- **Data Protocol**:  
  Defines how messages are structured when sent between the client and server.

In the future, the simulation can be updated to support stronger encryption protocols like WPA2 or WPA3.

