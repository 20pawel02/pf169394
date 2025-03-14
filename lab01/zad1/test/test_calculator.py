import unittest
from zad1.src.calculator import Kalkulator


class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalku = Kalkulator()

    def test_dodawanie(self):
        self.assertEqual(self.kalku.dodawanie(3, 4), 7)

    def test_odejmowanie(self):
        self.assertEqual(self.kalku.odejmowanie(-1, 9), 19)

    def test_mnozenie(self):
        self.assertEqual(self.kalku.mnozenie(3, 4), 12)

    def test_dzielenie_0(self):
        with self.assertRaises(ValueError):
            self.kalku.dzielenie(1, 0)

if __name__ == '__main__':
    unittest.main()