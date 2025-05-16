class Review:
    def __init__(
            self, id: int, stars: int, comment: str
    ):
        self.id = id
        self.stars = stars
        self.comment = comment


class Reviews:
    def __init__(self):
        self.reviews_list = {}
        self.next_id = 1

    def add_review(self, id: int, stars: int, comment: str):
        """
        Dodaje nową recenzję lub nadpisuje istniejącą recenzję dla danego ID użytkownika.
        """
        # input validation
        if id is None or not isinstance(id, int) or id <= 0:
            raise ValueError("User ID must be a valid integer.")
        if not stars or not isinstance(stars, int) or stars <= 0 or stars > 5:
            raise ValueError("Stars must be a valid integer between 1 and 5.")
        if not comment or not isinstance(comment, str):
            raise ValueError("Comment must be a string.")

        # dodanie/aktualizacja recenzji
        self.reviews_list[id] = Review(id, stars, comment)

    def edit_review(self, id: int, stars: int, comment: str):
        """
        Modyfikuje istniejącą recenzję. Rzuca KeyError, jeśli recenzja nie istnieje.
        """
        if id is None or id not in self.reviews_list:
            raise KeyError("Review with this ID does not exist.")

        # input validation
        if not stars or not isinstance(stars, int) or stars <= 0 or stars > 5:
            raise ValueError("Stars must be a valid integer between 1 and 5.")
        if not comment or not isinstance(comment, str):
            raise ValueError("Comment must be a string.")

        # aktualizacja recenzji
        self.reviews_list[id].stars = stars
        self.reviews_list[id].comment = comment

    def delete_review(self, id: int):
        """
        Usuwa recenzję. Rzuca KeyError, jeśli recenzja nie istnieje.
        """
        if id is None or id not in self.reviews_list:
            raise KeyError("Review with this ID does not exist.")
        del self.reviews_list[id]

    def get_review(self, id: int):
        """
        Pobiera recenzję użytkownika. Zwraca None, jeśli recenzja nie istnieje.
        """
        if id is None:
            raise TypeError("Review ID must be a valid integer.")
        return self.reviews_list.get(id, None)
