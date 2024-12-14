# WEP protocol

## How does it work ?

1. **Key Generation**
    - A shared secret key is established between the client and the access point.

2. **Initialization Vector (IV)**
    - A 24-bit IV is generated for each packet.

3. **Key Concatenation**
    - The IV is concatenated with the shared key to create an input for encryption.

4. **Key Stream Generation**
    - The RC4 algorithm generates a pseudo-random key stream.

5. **Data Encryption**
    - The plaintext and its CRC are encrypted using XOR with the key stream.

6. **Data Transmission**
    - The encrypted data and the IV (in plaintext) are sent to the receiver.

7. **Decryption**
    - The receiver reconstructs the key stream using the IV and shared key, decrypting the data with XOR.

8. **CRC Validation**
    - The receiver verifies the integrity of the data using the decrypted CRC.