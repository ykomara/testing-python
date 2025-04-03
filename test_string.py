import unittest

class TestString(unittest.TestCase):
    def test_should_capitalize_string(self):
        string="hello"
        expected_out="Hello"
        self.assertEqual(string.capitalize(),expected_out)

    def test_should_upper_string(self):
        string="hello"
        expected_out="HELLO"
        self.assertEqual(string.upper(), expected_out)