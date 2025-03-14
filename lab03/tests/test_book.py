import unittest
from src.book import Book

class TestBookInitialization(unittest.TestCase):
    """Test cases for the Book class initialization and methods."""

    def test_book_init(self):
        """Test that a Book object is initialized with the correct title and page count."""
        book_pride_and_prejudice = Book("Pride and Prejudice", 432)
        self.assertEqual(book_pride_and_prejudice.title, "Pride and Prejudice")
        self.assertEqual(book_pride_and_prejudice.page_count, 432)

    def test_calculate_reading_time(self):
        """Test the calculate_reading_time method for correct reading time calculation."""
        book_pride_and_prejudice = Book("Pride and Prejudice", 432)
        book_animal_farm = Book("Animal Farm", 112)
        self.assertAlmostEqual(book_pride_and_prejudice.calculate_reading_time(), 216, places=2)
        self.assertAlmostEqual(book_animal_farm.calculate_reading_time(), 56, places=2)

    def test_add_author(self):
        """Test adding a single author to the Book."""
        book_pride_and_prejudice = Book("Pride and Prejudice", 432)
        book_pride_and_prejudice.add_author("Jane Austen")
        self.assertEqual(book_pride_and_prejudice.authors, ["Jane Austen"])

    def test_add_mutlti_authors(self):
        """Test adding multiple authors to the Book."""
        book = Book("test1", 73)
        authors = ["George Orwell", "Aldous Huxley", "Ray Bradbury"]
        for author in authors:
            book.add_author(author)
        for author in authors:
            self.assertIn(author, book.authors)

    def test_add_author_error(self):
        """Test that adding an empty author raises a ValueError."""
        book = Book("test_book", 10)
        with self.assertRaises(ValueError) as context:
            book.add_author(" ")
            book.add_author("")
        self.assertEqual(str(context.exception), "Author name cannot be empty")

if __name__ == '__main__':
    unittest.main()