# Cryptographic Algorithm

## Diffie-Hellman Exchange Method

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

## RC4

RC4 is a stream cipher that generates a pseudo-random key stream to encrypt or decrypt data.

### How RC4 Algorithm Works

RC4 is a stream cipher that generates a pseudo-random key stream to encrypt or decrypt data. 

#### 1. **Key Scheduling Algorithm (KSA)**
- The algorithm initializes a permutation array `S` of size 256 (values 0 to 255).
- A secret key is used to shuffle this array. The shuffling ensures the key influences the final state of `S`.

#### 2. **Pseudo-Random Generation Algorithm (PRGA)**
- Once the `S` array is initialized, RC4 generates a key stream (pseudo-random bytes).
- The key stream is produced byte by byte and XORed with the plaintext (or ciphertext) to encrypt or decrypt.

#### 3. **Encryption or Decryption**
- The generated key stream is XORed with the plaintext to produce ciphertext during encryption.
- For decryption, the same key stream is XORed with the ciphertext to recover the plaintext (RC4 is symmetric).

