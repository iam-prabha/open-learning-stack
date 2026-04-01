# exercise.py - Practice Testing

import unittest
from unittest.mock import MagicMock

# Function to test: returns True if string is a palindrome
def is_palindrome(s):
    if not isinstance(s, str):
        return False
    clean_s = "".join(filter(str.isalnum, s)).lower()
    return clean_s == clean_s[::-1]

# TODO 1: Create a class 'TestPalindrome(unittest.TestCase)'
# class TestPalindrome(unittest.TestCase):
#     ...

# TODO 2: Add a test 'test_valid_palindrome' to test "Racecar" and "A man a plan a canal Panama".
# (Hint: use self.assertTrue())

# TODO 3: Add a test 'test_invalid_palindrome' to test "hello" and "python".
# (Hint: use self.assertFalse())

# TODO 4: Add a test 'test_non_string' to ensure is_palindrome(123) returns False.

# TODO 5: Write a simple pytest-style function 'test_basic_math' that
# asserts 2 + 2 == 4.
# def test_basic_math():
#     ...

# TODO 6: Use MagicMock to mock a 'database.get_user(id)' call in a test.
# def get_user_email(db, user_id):
#     user = db.get_user(user_id)
#     return user['email']

# CHALLENGE: Create a test for a function that raises 'ValueError' 
# and use 'self.assertRaises' to verify it.

# --- Verification ---
if __name__ == '__main__':
    print("Run this file to execute the unittest suite.")
    # unittest.main()
