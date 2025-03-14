class Book:
    def __init__(self, title: str, page_count: int):
        self.title = title
        self.page_count = page_count

    def calculate_reading_time(self) -> float:
        return self.page_count / 2
