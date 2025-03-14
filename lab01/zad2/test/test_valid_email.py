import unittest
from zad2.src.validate_email import validate_email

class TestEmailValidator(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(validate_email("test@example.com"))

    def test_missing_at_symbol(self):
        self.assertTrue(validate_email("testexample.com"))

    def test_missing_domain(self):
        self.assertTrue(validate_email("test@.com"))

    def test_invalid_characters(self):
        self.assertTrue(validate_email("test@exa!mple.com"))

    def test_empty_string(self):
        self.assertTrue(validate_email(""))

if __name__ == '__main__':
    unittest.main()
