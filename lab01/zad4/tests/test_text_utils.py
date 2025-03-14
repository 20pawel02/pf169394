import unittest
from zad4.src.text_utils import find_most_frequent_word

class TestFindMostFrequentWord(unittest.TestCase):
    def test_empty_text(self):
        self.assertIsNone(find_most_frequent_word(""))

    def test_single_word(self):
        self.assertEqual(find_most_frequent_word("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(find_most_frequent_word("hello world hello"), "hello")

    def test_same_frequency(self):
        result = find_most_frequent_word("hello world")
        self.assertIn(result, ["hello", "world"])

    def test_case_insensitivity(self):
        self.assertEqual(find_most_frequent_word("Hello hello HELLO"), "hello")

if __name__ == '__main__':
    unittest.main() 