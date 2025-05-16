class Review:
    def __init__(self, id: int, stars: int, comment: str):
        self.id = id
        self.stars = stars
        self.comment = comment


class Reviews:
    def __init__(self):
        self.reviews_list = {}

    def add_review(self, id: int, stars: int, comment: str):
        # input validation
        if not id or not isinstance(id, int) or id < 0:
            raise ValueError("User ID must be a valid integer.")
        if not isinstance(stars, int) or stars <= 0 or stars > 5:
            raise ValueError("Stars must be a valid integer between 1 and 5.")
        if not comment or not isinstance(comment, str):
            raise ValueError("Comment must be a string.")
        if len(comment) > 10:  # max length of 10 characters for testing purposes
            raise ValueError("Comment can be max 10 characters long.")

        # checking conflicting reviews
        if id in self.reviews_list:
            raise ValueError(f"Review {id} was already added.")

        # creating new review
        self.reviews_list[id] = Review(id, stars, comment)

    def edit_review(self, id: int, stars: int, comment: str):
        # check if review exists
        if id not in self.reviews_list:
            return []

        # input validation
        if not stars or not isinstance(stars, int) or stars <= 0 or stars > 5:
            raise ValueError("Stars must be a positive integer bigger than 0 and lower than 5.")
        if not comment or not isinstance(comment, str):
            raise ValueError("Comment must be a string.")

        # updating review
        self.reviews_list[id].stars = stars
        self.reviews_list[id].comment = comment

    def delete_review(self, id: int):
        if id not in self.reviews_list:
            #raise ValueError(f"Review {id} wasn't found.")
            return
        del self.reviews_list[id]

    def get_review(self, id: int):
        return self.reviews_list.get(id, None)