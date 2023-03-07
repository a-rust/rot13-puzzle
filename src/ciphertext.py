# For now, just resort to using this for importing modules

from src.plaintext import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))


# Function for applying ROT13 encryption algorithm to the randomly generated plaintext
def rot13_encrypt(plaintext: str) -> str:
    ciphertext = ""
    for char in plaintext:
        index = alphabet.find(char)
        ciphertext += alphabet[(index + 13) % len(alphabet)]
    return ciphertext
