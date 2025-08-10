import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def b64encode(b: bytes) -> str:
    return base64.b64encode(b).decode('utf-8')

def b64decode(s: str) -> bytes:
    return base64.b64decode(s.encode('utf-8'))

def encrypt_bytes(plaintext: bytes, key_b64: str) -> bytes:
    key = b64decode(key_b64)
    nonce = get_random_bytes(12)  # recommended size for GCM
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    # store: nonce || tag || ciphertext
    return nonce + tag + ciphertext

def decrypt_bytes(blob: bytes, key_b64: str) -> bytes:
    key = b64decode(key_b64)
    nonce = blob[:12]
    tag = blob[12:28]
    ciphertext = blob[28:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext
