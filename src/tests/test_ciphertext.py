# Importing ciphertext.py from the parent directory ./src

from src.ciphertext import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))


# Tests to check edge cases of ROT13 algorithm
# Case 1: Every char x in plaintext is within the first (24-12)=12 letters of the alphabet
# Case 2: There exists some char x in plaintext within the first (24-12)=12 letters of the alphabet, and there exists some char y in plaintext within the last (24-12)=12 letters of the alphabet
# Case 3: Every char x in plaintext is within the last (24-12)=12 letters of the alphabet
# Case 4: Duplicate chars
def test_rot13_encrypt():
    assert rot13_encrypt("abc") == "nop"
    assert rot13_encrypt("aqr") == "nde"
    assert rot13_encrypt("xyz") == "klm"
    assert rot13_encrypt("aab") == "nno"
