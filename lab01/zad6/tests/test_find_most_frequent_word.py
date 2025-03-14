import unittest
from zad6.src.find_most_frequent_word import find_most_frequent_word

class TestFindMostFrequentWord(unittest.TestCase):
    def test_empty_text(self):
        self.assertIsNone(find_most_frequent_word(""))

    def test_single_word(self):
        self.assertEqual(find_most_frequent_word("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(find_most_frequent_word("this is a test this is only a test"), "this")

    def test_same_frequency(self):
        result = find_most_frequent_word("apple orange banana apple orange banana")
        self.assertIn(result, ["apple", "orange", "banana"])

if __name__ == "__main__":
    unittest.main()
