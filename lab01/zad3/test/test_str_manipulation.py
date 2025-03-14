import unittest
from zad3.src.string_manipulation import StringManipulation

class TestStringManipulation(unittest.TestCase):
    def setUp(self):
        self.manipulator = StringManipulation()

    def test_odwrocenie(self):
        self.assertEqual(self.manipulator.reverse_string("jajko"), "okjaj")

    def test_licznik_slow(self):
        self.assertEqual(self.manipulator.count_words("bajo jajo ja ci dam bajo jajo"), 6)

    def test_slowa_capslock(self):
        self.assertCountEqual(self.manipulator.capitalized_words("POLSKA GoRA"), "POLSKA GoRA")

if __name__ == '__main__':
    unittest.main()