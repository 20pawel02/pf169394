import unittest
from zad9.src.is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def is_palindrome_true(self):
        self.assertTrue(is_palindrome("kajak"))

    def is_palindrome_false(self):
        self.assertFalse(is_palindrome("abcde"))


if __name__ == '__main__':
    unittest.main()
