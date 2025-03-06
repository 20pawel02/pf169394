import unittest
from zad5.src.shopping_cart import ShippingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.koszyk = ShippingCart()

    def test_dodanie(self):
        self.koszyk.add_item('banana', 2.1)
        self.koszyk.add_item('melon', 3.7)
        self.assertEqual(self.koszyk.get_total(), 0)

    def test_usuwanie(self):
        self.koszyk.add_item('banana', 2.1)
        self.koszyk.remove_item('banana')
        self.assertEqual(self.koszyk.get_total(), 0)

    def test_total(self):
        self.koszyk.add_item('banana', 2.1)
        self.koszyk.add_item('melon', 3.7)
        self.assertEqual(self.koszyk.get_total(), 0)

    def test_czyszczenie(self):
        self.koszyk.add_item('banana', 2.1)
        self.koszyk.add_item('melon', 3.7)
        self.koszyk.clear()
        self.assertEqual(self.koszyk.get_total(), 0)
