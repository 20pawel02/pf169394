import unittest
from zad8.src.BankAccount import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.konto = BankAccount()

    def test_deposit(self):
        self.konto.deposit(2137)
        self.assertEqual(self.konto.get_balance(), 2137)

    def test_withdraw(self):
        self.konto.deposit(2)
        self.konto.withdraw(5)
        self.assertEqual(self.konto.get_balance(), -3)

    def test_initial_balance(self):
        self.assertEqual(self.konto.get_balance(), 0)


if __name__ == "__main__":
    unittest.main()
