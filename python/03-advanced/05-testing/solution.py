# solution.py - Testing answers

import unittest
from unittest.mock import MagicMock

# The function under test
def is_palindrome(s):
    if not isinstance(s, str):
        return False
    clean_s = "".join(filter(str.isalnum, s)).lower()
    return clean_s == clean_s[::-1]

# TODO 1-4: Unit tests
class TestPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_invalid_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))

    def test_non_string(self):
        self.assertFalse(is_palindrome(123))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

# TODO 5: Pytest style
def test_basic_math():
    assert 2 + 2 == 4

# TODO 6: Mocking
def get_user_email(db, user_id):
    user = db.get_user(user_id)
    return user['email']

class TestDatabase(unittest.TestCase):
    def test_get_user_email(self):
        mock_db = MagicMock()
        mock_db.get_user.return_value = {'id': 1, 'email': 'test@example.com'}
        
        email = get_user_email(mock_db, 1)
        self.assertEqual(email, 'test@example.com')
        mock_db.get_user.assert_called_with(1)

# CHALLENGE
def strictly_positive(n):
    if n <= 0:
        raise ValueError("Must be positive")
    return n

class TestValueErrors(unittest.TestCase):
    def test_strictly_positive_error(self):
        with self.assertRaises(ValueError):
            strictly_positive(-5)

# --- Verification ---
if __name__ == '__main__':
    print("--- Running tests ---")
    unittest.main()

print("\n--- Why it works ---")
print("1. unittest.TestCase: Provides assertions like assertEqual and assertRaises.")
print("2. Mocking (MagicMock): Replaces slow or unreliable dependencies (DB, API) with predictable objects.")
print("3. Pytest: Modern standard that favors simple functions over classes, making tests easier to write.")
print("4. Unit vs Integration: These are 'unit' tests because they isolate the logic from the rest of the world.")
