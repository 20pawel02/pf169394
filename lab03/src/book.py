class Book:
    """A class representing a book with a title, page count, and authors."""

    def __init__(self, title: str, page_count: int):
        """Initialize a Book with a title and page count."""
        self.title = title
        self.page_count = page_count
        self.authors = []

    def calculate_reading_time(self) -> float:
        """Calculate the estimated reading time based on 2 pages per minute."""
        return self.page_count / 2

    def add_author(self, author: str):
        """Add an author to the book's list of authors.

        Raises:
            ValueError: If the author's name is empty or only whitespace.
        """
        if not author.strip():
            raise ValueError("Author name cannot be empty")
        self.authors.append(author)