# example.py - Unit Testing in Python

import unittest
from unittest.mock import MagicMock

# Function to test
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a + b

# 1. Using standard unittest
class TestMathOperations(unittest.TestCase):
    def test_add_success(self):
        self.assertEqual(add(10, 5), 15)
    
    def test_add_failure(self):
        with self.assertRaises(TypeError):
            add(10, "5")

# 2. Pytest style (simple functions + assert)
# To run: pytest example.py
def test_add_pytest():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

# 3. Mocking (isolating code from dependencies)
class APIClient:
    def get_status(self):
        # Imagine this makes a real web request
        return "Offline"

def check_system(client: APIClient):
    status = client.get_status()
    if status == "Online":
        return "Everything is OK"
    return "System Down"

class TestSystem(unittest.TestCase):
    def test_check_system(self):
        # Create a mock client instead of a real one
        mock_client = MagicMock()
        mock_client.get_status.return_value = "Online"
        
        result = check_system(mock_client)
        self.assertEqual(result, "Everything is OK")
        mock_client.get_status.assert_called_once()

if __name__ == '__main__':
    # Run the unittest suite
    unittest.main()
