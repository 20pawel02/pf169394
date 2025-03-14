import unittest
from src.book import Book

class TestBookInitialization(unittest.TestCase):
    def test_book_init(self):
        book_pride_and_prejudice = Book("Pride and Prejudice", 432)
        self.assertEqual(book_pride_and_prejudice.title, "Pride and Prejudice")
        self.assertEqual(book_pride_and_prejudice.page_count, 432)

    def test_calculate_reading_time(self):
        book_pride_and_prejudice = Book("Pride and Prejudice", 432)
        book_animal_farm = Book("Animal Farm", 112)
        self.assertAlmostEqual(book_pride_and_prejudice.calculate_reading_time(), 216, places=2)
        self.assertAlmostEqual(book_animal_farm.calculate_reading_time(), 56, places=2)

    def test_add_author(self):
        book_pride_and_prejudice = Book("Pride and Prejudice", 432)
        book_pride_and_prejudice.add_author("Jane Austen")
        self.assertEqual(book_pride_and_prejudice.authors, ["Jane Austen"])

    def test_add_mutlti_authors(self):
        book = Book("test1", 73)
        authors = ["George Orwell", "Aldous Huxley", "Ray Bradbury"]
        for author in authors:
            book.add_author(author)
        for author in authors:
            self.assertIn(author, book.authors)

    def test_add_author_error(self):
        book = Book("test_book", 10)
        with self.assertRaises(ValueError) as context:
            book.add_author(" ")
            book.add_author("")
        self.assertEqual(str(context.exception), "Author name cannot be empty")

if __name__ == '__main__':
    unittest.main()