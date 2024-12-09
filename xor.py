def xor_encrypt_decrypt(message, key):
    key = str(key)
    encrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, key * len(message)))
    return encrypted