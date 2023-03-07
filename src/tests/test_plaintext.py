# How to access plaintext.py (module in parent directory)
# Make sure that you have '__init__.py' in your directory, and in the parent directory (all the way up to the module you want to access)

from src.plaintext import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))


# Test to check that the index of each char gets matched to the correct index of the plaintext
def test_generate_string():
    char_list = generate_random_chars()
    plaintext = chars_to_string(char_list)
    for char in char_list:
        assert char_list.index(char) == plaintext.find(char)
