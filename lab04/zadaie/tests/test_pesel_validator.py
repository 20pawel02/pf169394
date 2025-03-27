import unittest
from zadaie.src.pesel_validator import PeselValidator

class TestPeselValidator(unittest.TestCase):
    def test_pesel_format(self):
        self.assertTrue(PeselValidator.validate_format("12345678901"))
        self.assertFalse(PeselValidator.validate_format("123456789"))
        self.assertFalse(PeselValidator.validate_format("1234567890123"))
        self.assertFalse(PeselValidator.validate_format(""))

    def test_check_digit(self):
        self.assertTrue(PeselValidator.validate_check_digit("44051401458"))
        self.assertTrue(PeselValidator.validate_check_digit("02070803628"))
        self.assertFalse(PeselValidator.validate_check_digit("44051401459"))
        self.assertFalse(PeselValidator.validate_check_digit("02070803627"))

    def test_birth_date(self):
        self.assertTrue(PeselValidator.validate_birth_date("44051401458"))
        self.assertFalse(PeselValidator.validate_birth_date("02270803628"))
        self.assertFalse(PeselValidator.validate_birth_date("99912312345"))
        self.assertFalse(PeselValidator.validate_birth_date("44130101234"))
        self.assertFalse(PeselValidator.validate_birth_date("44043201234"))
        self.assertFalse(PeselValidator.validate_birth_date("44022901234"))
        self.assertFalse(PeselValidator.validate_birth_date("00023001234"))

    def test_gender(self):
        male_pesel = "12345612345"
        female_pesel = "12345612344"

        self.assertEqual(PeselValidator.get_gender(male_pesel), "M")
        self.assertEqual(PeselValidator.get_gender(female_pesel), "F")

    def test_is_valid(self):
        # Valid PESEL
        self.assertTrue(PeselValidator.is_valid("44051401458"))
        self.assertTrue(PeselValidator.is_valid("02070803628"))

        # Invalid format
        self.assertFalse(PeselValidator.is_valid("1234567890"))
        self.assertFalse(PeselValidator.is_valid("123456789012"))

        # Invalid check digit
        self.assertFalse(PeselValidator.is_valid("44051401459"))

        # Invalid birth date
        self.assertFalse(PeselValidator.is_valid("44130101234"))
        self.assertFalse(PeselValidator.is_valid("44043201234"))

    def test_edge_cases(self):
        # Test PESEL from different centuries
        self.assertTrue(PeselValidator.is_valid("44051401458"))  # 20th century
        self.assertTrue(PeselValidator.is_valid("02270803628"))  # 21st century
        self.assertTrue(PeselValidator.is_valid("81020312345"))  # 19th century (1800s)
        self.assertTrue(PeselValidator.is_valid("61020312345"))  # 22nd century (2100s)

        # Test PESEL with a birth date of February 29 in a leap year
        self.assertTrue(PeselValidator.is_valid("44022912345"))  # Valid leap year date
        self.assertFalse(PeselValidator.is_valid("44022812345"))  # Invalid non-leap year date
        self.assertFalse(PeselValidator.is_valid("44022912346"))  # Invalid leap year date (wrong check digit)

if __name__ == "__main__":
    unittest.main()