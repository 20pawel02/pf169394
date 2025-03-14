import unittest
from src.book import Book

class TestBookInitialization(unittest.TestCase):
    def test_book_init(self):
        book = Book("Pride and Prejudice", 432)
        self.assertEqual(book.title, "Pride and Prejudice")
        self.assertEqual(book.page_count, 432)

    def test_calculate_reading_time(self):
        book_pride_and_prejudice = Book("Pride and Prejudice", 432)
        book_animal_farm = Book("Animal Farm", 112)
        self.assertAlmostEqual(book_pride_and_prejudice.read_time, 216, places=3)
        self.assertAlmostEqual(book_animal_farm.read_time, 56, places=3)


if __name__ == '__main__':
    unittest.main()