# Cryptographic Algorithm

```mermaid
mindmap
  root((Wi-Fi Encryption Protocol))
    WEP
      encryption(RC4 Key)
      functions
        KSA(Key Scheduling Algorithm)
        PRGA(Pseudo-Random Generation Algorithm)
        XOR(Bitwise XOR Operation)
    WPA1
      encryption(TKIP: Temporal Key Integrity Protocol)
      functions
        MIC(Message Integrity Check)
        TSC(Temporal Sequence Counter)
        RC4(TKIP uses RC4 for encryption)
    WPA2
      encryption(AES: Advanced Encryption Standard)
      protocol(CCMP: Counter Mode with Cipher Block Chaining Message Authentication Code Protocol)
      enterpriseMode(Enterprise Mode: 802.1X)
      personalMode(Personal Mode: WPA-PSK)
      functions
        PMK(Pairwise Master Key)
        PTK(Pairwise Transient Key)
        GTK(Group Temporal Key)
    WPA3
      encryption(192-bit Security Suite for sensitive networks)
      SAE(SAE: Simultaneous Authentication of Equals)
      functions
        OWE(Opportunistic Wireless Encryption)
        H2E(Hash-to-Element Protocol)
        PMF(Protected Management Frames)

```

## XOR cipher

### Code

```
def xor_encrypt_decrypt(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return encrypted_text
```

- takes `text` as string and `key` as string, as parameters.
- `ord(char)` finds unicode position for given character.
- `ord(text[i]) ^ ord(key[i % len(key)]` does a bitwise XOR operation between the Unicode value of the current character in the text and the corresponding character in the key.
- `chr(number)` finds the character for a given position.
- returns `encrypted_text`
