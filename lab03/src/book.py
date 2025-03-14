class Book:
    def __init__(self, title: str, page_count: int):
        self.title = title
        self.page_count = page_count
        self.authors = []

    def calculate_reading_time(self) -> float:
        return self.page_count / 2

    def add_author(self, author: str):
        if not author.strip():
            raise ValueError("Author name cannot be empty")
        self.authors.append(author)