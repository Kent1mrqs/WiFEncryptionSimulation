# Cryptographic Algorithm

## XOR cipher

Here is the code : 
```
def xor_encrypt_decrypt(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return encrypted_text
```

- `ord(char)` finds unicode position for given character.
- `ord(text[i]) ^ ord(key[i % len(key)]` does XOR operation between i position
- `chr(number)` finds the character for a given position.
- 

## RC4