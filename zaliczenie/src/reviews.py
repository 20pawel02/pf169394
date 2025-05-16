class Review:
<<<<<<< HEAD
    """
    Represents a single review with its details.

    Attributes:
        id (int): The unique identifier for the review.
        stars (int): Rating of the review from 1 to 5.
        comment (str): Textual comment for the review.
    """
    def __init__(self, id: int, stars: int, comment: str):
=======
    def __init__(
            self, id: int, stars: int, comment: str
    ):
>>>>>>> parent of 1d01520 (final)
        self.id = id
        self.stars = stars
        self.comment = comment

class Reviews:
    """
    Manages a collection of reviews with methods to add, edit, and delete reviews.

    Attributes:
        reviews_list (dict): A dictionary storing reviews, keyed by user ID.
    """
    def __init__(self):
        self.reviews_list = {}
        self.next_id = 1

    def add_review(self, id: int, stars: int, comment: str):
        """
        Add a new review for a user.

        Args:
            id (int): User's unique identifier.
            stars (int): Rating from 1 to 5.
            comment (str): Review comment.

        Raises:
            ValueError: If input validation fails or a review already exists for the user.
        """
        # input validation
        if not id or not isinstance(id, int) or id < 0:
            raise ValueError("User ID must be a valid integer.")
        if not stars or not isinstance(stars, int) or stars <= 0 or stars > 5:
            raise ValueError("Stars must be a valid integer between 1 and 5.")
        if not comment or not isinstance(comment, str):
            raise ValueError("Comment must be a string.")

        # checking conflicting reviews
        if id in self.reviews_list:
            raise ValueError(f"Review {id} was already added.")

        # creating new review
        self.reviews_list[id] = Review(id, stars, comment)

    def edit_review(self, id: int, stars: int, comment: str):
        """
        Edit an existing review for a user.

        Args:
            id (int): User's unique identifier.
            stars (int): New rating from 1 to 5.
            comment (str): New review comment.

        Raises:
            ValueError: If input validation fails.
            Returns an empty list if the review does not exist.
        """
        # check if review exists
        if id not in self.reviews_list:
            raise ValueError(f"Review {id} was not found.")

        # input validation
        if not stars or not isinstance(stars, int) or stars <= 0 or stars > 5:
            raise ValueError(
                "Stars must be a positive integer bigger than 0 and lower than 5."
            )
        if not comment or not isinstance(comment, str):
            raise ValueError("Comment must be a string.")

        # updating review
        self.reviews_list[id].stars = stars
        self.reviews_list[id].comment = comment

    def delete_review(self, id: int):
        """
        Delete a review for a given user ID.

        Args:
            id (int): User's unique identifier.
        """
        if id not in self.reviews_list:
<<<<<<< HEAD
            return
=======
            raise ValueError(f"Review {id} wasn't found.")
>>>>>>> parent of 1d01520 (final)
        del self.reviews_list[id]

    def get_review(self, id: int):
        """
        Retrieves a review for a given user ID.

        Args:
            id (int): User's unique identifier.

        Returns:
            Review: The review for the given user ID, or None if no review exists.
        """
        return self.reviews_list.get(id, None)
