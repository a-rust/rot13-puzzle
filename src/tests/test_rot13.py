# How to access plaintext.py (module in parent directory)
# Make sure that you have '__init__.py' in your directory, and in the parent directory (all the way up to the module you want to access)
# Use import <parent_directory>.<file> to access a file from a parent directory, and then use the syntax below when calling something from that file
import src.rot13

# Test to check that the index of each char gets matched to the correct index of the plaintext


def test_generate_string():
    # If you want to call something within a file from the parent directory, use the
    # <parent_directory>.<file>.<something> syntax
    char_list = src.rot13.generate_random_chars()
    plaintext = src.rot13.chars_to_string(char_list)
    for char in char_list:
        # No need to worry about duplicates, since random.sample returns unique characters
        #   And our list has only 5 elements, whereas the sample set contains 25 elements
        assert char_list.index(char) == plaintext.find(char)


def test_rot13_encrypt():
    assert src.rot13.rot13_encrypt("abc") == "nop"
    assert src.rot13.rot13_encrypt("aqr") == "nde"
    assert src.rot13.rot13_encrypt("xyz") == "klm"
    assert src.rot13.rot13_encrypt("aab") == "nno"
