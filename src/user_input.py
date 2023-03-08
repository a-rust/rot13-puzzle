# When importing modules within same directory, do it like this:
# from <sibling_file_name> import <whatever>
from rot13 import *


# Function to create rot13 puzzles for the user
def create_puzzles():
    plaintext_entries: list[str] = []
    ciphertext_entries: list[str] = []
    answer_entries: list[int] = []
    database_entries = [ciphertext_entries, plaintext_entries, answer_entries]
    number_of_puzzles: int = int(
        input("How many rot13 puzzles would you like?: "))
    for number in range(0, number_of_puzzles):
        rand_chars = generate_random_chars()
        # Appending plaintext to plaintext list
        plaintext_entries.append(chars_to_string(rand_chars))
        # Appending ciphertext to ciphertext list
        ciphertext_entries.append(rot13_encrypt(
            plaintext_entries[-1]))
        answer: str = str(input(f"Decrypt '{ciphertext_entries[-1]}': "))
        # Highest index of plaintext list should be the decryption of the highest index of ciphertext list
        if answer == plaintext_entries[-1]:
            print('Correct!')
            # If correct, append true (1) to answers list
            answer_entries.append(1)
        else:
            print('Sorry, incorrect.')
            # If incorrect, append false (0) to answers list
            answer_entries.append(0)
    return database_entries
