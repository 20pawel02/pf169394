import unittest
from zad4.src.fib import Fibonacci

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibo = Fibonacci()

    def test_n_0(self):
        self.assertEqual(self.fibo(0), 0)

    def test_n_1(self):
        self.assertEqual(self.fibo(1), 1)

    def test_n_3(self):
        self.assertEqual(self.fibo(3), 2)
    
    def test_n_ujemne(self):
        with self.assertRaises(ValueError):
            self.fibo(-1)