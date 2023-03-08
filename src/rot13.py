import random

# The characters of each random string will be sampled from the English alphabet
alphabet = ("abcdefghijklmnopqrstuvwxyz")


# Function for generating a random 5-character string using the English alphabet
def generate_random_chars() -> list:
    char_list: list[str] = random.sample(alphabet, 3)
    return char_list


# Function for concatenating chars from list into a single string
def chars_to_string(char_list: list[str]) -> str:
    plaintext: str = ""
    for char in char_list:
        plaintext += char
    return plaintext


# Function for encrypting the plaintext using rot13
def rot13_encrypt(plaintext: str) -> str:
    ciphertext = ""
    for char in plaintext:
        index = alphabet.find(char)
        ciphertext += alphabet[(index + 13) % len(alphabet)]
    return ciphertext
