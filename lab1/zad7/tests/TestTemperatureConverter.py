import unittest
from zad7.src.TemperatureConverter import TemperatureConverter

class TestTemperatureConverter(unittest.TestCase):
    def test_celc_to_fahr(self):
        self.assertAlmostEqual(TemperatureConverter.celsius_to_fahrenheit(1), 33.8, places=2)

    def test_celc_to_fahr(self):
        self.assertAlmostEqual(TemperatureConverter.fahrenheit_to_celsius(33.8), 1, places=2)

    def test_celc_to_fahr(self):
        self.assertAlmostEqual(TemperatureConverter.celsius_to_kelvin(1), 274.15, places=2)

    def test_celc_to_fahr(self):
        self.assertAlmostEqual(TemperatureConverter.kelvin_to_celsius(274.15), 1)

if __name__ == "__main__":
    unittest.main() 