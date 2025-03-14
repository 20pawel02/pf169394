import unittest
from src.book import Book

class TestBookInitialization(unittest.TestCase):
    def test_book_init(self):
        book = Book("Pride and Prejudice", 432)
        self.assertEqual(book.title, "Pride and Prejudice")
        self.assertEqual(book.page_count, 432)