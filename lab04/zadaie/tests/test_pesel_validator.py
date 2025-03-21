import unittest
from zadaie.src.pesel_validator import PeselValidator

class TestPeselValidator(unittest.TestCase):
    def test_pesel_format(self):
        self.assertTrue(PeselValidator.validate_format("12345678901"))
        self.assertFalse(PeselValidator.validate_format("123456789"))
        self.assertFalse(PeselValidator.validate_format("1234567890123"))
        self.assertFalse(PeselValidator.validate_format(""))
        