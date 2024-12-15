def xor_encrypt_decrypt(text, key):
    key = str(key)
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return encrypted_text

def ksa(key,S):
    key = [ord(char) for char in key] # string to byte
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256 # Now, j relies on the key
        S[i], S[j] = S[j], S[i]  # Swap S[i] and S[j]
    return S

def prga(S, length):
    i,j = 0,0
    key_stream = []

    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        key_stream_byte = S[(S[i] + S[j]) % 256]
        key_stream.append(key_stream_byte)

    return key_stream

def rc4(text, key):
    S = list(range(256))
    S = ksa(str(key),S)
    keystream = prga(S,len(text))
    encrypted = xor_encrypt_decrypt(text,keystream)

    return encrypted