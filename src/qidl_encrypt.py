"""
Quantum Isoca-Dodecahedral Encryption (QIDL)
Part of the TetraCrypt PQC Nexus
Now hardened with entropy salt injection.
"""

import numpy as np
import time
import os

def generate_isoca_dodecahedral_key(seed: int = 42):
    """
    Generate a pseudo-random dodecahedral structure key based on golden ratio encoding.
    """
    np.random.seed(seed)
    phi = (1 + np.sqrt(5)) / 2
    angles = np.linspace(0, 2 * np.pi, 20)
    key = np.array([np.cos(phi * angles), np.sin(phi * angles)]).T
    return key

def generate_entropy_salt(length: int = 8) -> str:
    """
    Generate a random entropy-based salt using system time and os randomness.
    """
    random_bytes = os.urandom(length)
    timestamp = str(time.time()).encode()
    entropy = ''.join([chr((b + t) % 256) for b, t in zip(random_bytes, timestamp)])
    return entropy

def qidl_encrypt(message: str, key: np.ndarray, salt: str = None):
    """
    Quantum layer simulation using rotational golden-ratio projection.
    Each character is transformed into a vector projection on a dodecahedron.
    Salt ensures unique encryption output even for identical messages.
    """
    if salt is None:
        salt = generate_entropy_salt()
    message += salt  # Append entropy salt to message

    encoded = []
    for i, char in enumerate(message):
        char_val = ord(char)
        point = key[i % len(key)]
        transformed = (char_val * point[0], char_val * point[1])
        encoded.append(transformed)
    return encoded, salt  # Return salt so decryption is possible

def qidl_decrypt(encoded_message, key: np.ndarray, salt: str = ''):
    """
    Reverse the dodecahedral projection and extract characters.
    Removes salt after decryption.
    """
    decoded = ''
    for i, (x, y) in enumerate(encoded_message):
        point = key[i % len(key)]
        char_val = round((x + y) / (point[0] + point[1]))
        decoded += chr(int(char_val) % 256)

    if salt and decoded.endswith(salt):
        decoded = decoded[:-len(salt)]
    return decoded
