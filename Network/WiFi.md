# WiFi

WiFi, short for "Wireless Fidelity," is a wireless communication technology that allows devices to connect to the internet and communicate with each other over a wireless network. It uses radio waves to transmit data between devices like smartphones, laptops, routers, and access points.

---

## Key Components of a WiFi Network

1. **WiFi Router or Access Point**
    - Acts as the central hub of the network.
    - Broadcasts the wireless signal and connects devices to the internet.

2. **WiFi Device (Client)**
    - A device (like a phone, laptop, or tablet) that connects to the router to access the network.

3. **Radio Signals**
    - WiFi uses radio waves in the 2.4 GHz or 5 GHz frequency bands to transmit data.

4. **Encryption Protocols**
    - Secure the communication between devices and prevent unauthorized access (e.g., WPA2, WPA3).

---

## Steps to Establish a WiFi Connection

1. **Scanning for Networks**
    - Devices search for available networks and display their names (SSIDs).

2. **Authentication**
    - For secured networks, users must provide a password. The router verifies the credentials using encryption protocols (e.g., WPA2).

3. **IP Address Assignment**
    - Once authenticated, the router assigns an IP address to the device using DHCP (Dynamic Host Configuration Protocol).

4. **Connection Established**
    - The device is now connected to the network and can access the internet or communicate with other devices.

---

## Security in WiFi

1. **Open Networks**
    - No password required; anyone can connect.
    - High risk of data interception.

2. **Secured Networks**
    - Require authentication and use encryption to secure data:
        - **WEP**: Outdated and insecure.
        - **WPA/WPA2**: Common and secure for most networks.
        - **WPA3**: The most secure standard available.

3. **Enterprise Networks**
    - Use advanced authentication methods like username/password or certificates for large organizations.

---

## WiFi Protocols and Standards

WiFi operates based on IEEE 802.11 standards. Here’s a quick summary of common WiFi standards:

| **Standard**  | **Frequency Band** | **Maximum Speed** | **Range**            |  
|---------------|--------------------|-------------------|----------------------|  
| 802.11b       | 2.4 GHz           | 11 Mbps          | Up to 35 meters     |  
| 802.11g       | 2.4 GHz           | 54 Mbps          | Up to 38 meters     |  
| 802.11n       | 2.4 GHz/5 GHz     | 600 Mbps         | Up to 70 meters     |  
| 802.11ac      | 5 GHz             | 1.3 Gbps         | Up to 35 meters     |  
| 802.11ax (WiFi 6)| 2.4 GHz/5 GHz  | 9.6 Gbps         | Up to 50 meters     |  

---

## WiFi Security Handshake

For secured networks, a **handshake process** occurs to establish encrypted communication:

1. **Authentication**
    - The router sends a challenge to the device.
    - The device responds by encrypting the challenge with the network key.
    - The router decrypts and verifies the response.

2. **Key Exchange**
    - Devices generate session keys for encrypted communication.

3. **Data Encryption**
    - All data transmitted between the device and router is encrypted using the session key.

