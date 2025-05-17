import unittest
from src.reviews import Reviews


class TestBaseFunctions(unittest.TestCase):
    def setUp(self):
        self.manager = Reviews()

    def test_add_review(self):
        self.manager.add_review(1, 5, "comment1")
        self.assertEqual(self.manager.reviews_list[1].stars, 5)
        self.assertEqual(self.manager.reviews_list[1].comment, "comment1")

    def test_edit_review(self):
        self.manager.add_review(1, 5, "comment1")
        self.manager.edit_review(1, 4, "updated")
        self.assertEqual(self.manager.reviews_list[1].stars, 4)
        self.assertEqual(self.manager.reviews_list[1].comment, "updated")

    def test_delete_review(self):
        self.manager.add_review(1, 5, "comment1")
        self.manager.delete_review(1)
        self.assertEqual(len(self.manager.reviews_list), 0)

    def test_get_reviews(self):
        self.manager.add_review(1, 5, "comment1")
        review = self.manager.get_review(1)
        self.assertEqual(review.id, 1)
        self.assertEqual(review.stars, 5)
        self.assertEqual(review.comment, "comment1")

    def test_multiple_reviews(self):
        self.manager.add_review(1, 5, "comment1")
        self.manager.add_review(2, 4, "comment2")
        self.manager.add_review(3, 3, "comment3")
        self.assertEqual(len(self.manager.reviews_list), 3)
        self.assertEqual(self.manager.reviews_list[1].stars, 5)
        self.assertEqual(self.manager.reviews_list[2].stars, 4)
        self.assertEqual(self.manager.reviews_list[3].stars, 3)

    def test_update_existing_review(self):
        self.manager.add_review(1, 5, "comment1")
        self.manager.add_review(1, 4, "updated")
        self.assertEqual(len(self.manager.reviews_list), 1)
        self.assertEqual(self.manager.reviews_list[1].stars, 4)
        self.assertEqual(self.manager.reviews_list[1].comment, "updated")


class TestInvalidInputs(unittest.TestCase):
    """
    Test suite for input validation in review management.

    These tests ensure that the review system correctly handles
    various invalid input scenarios, such as incorrect user IDs,
    star ratings, and comments.
    """

    def setUp(self):
        self.manager = Reviews()

    def test_invalid_id(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.add_review("invalid", 5, "comment1")

    def test_invalid_id1(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.add_review(-1, 5, "comment1")

    def test_invalid_id2(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.add_review(0, 5, "comment1")

    def test_invalid_id3(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.add_review(1.5, 5, "comment1")

    def test_invalid_id4(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.add_review(None, 5, "comment1")

    def test_invalid_star(self):
        with self.assertRaisesRegex(ValueError, "Stars must be a valid integer between 1 and 5."):
            self.manager.add_review(1, 6, "comment1")

    def test_invalid_star1(self):
        with self.assertRaisesRegex(ValueError, "Stars must be a valid integer between 1 and 5."):
            self.manager.add_review(1, -1, "comment1")

    def test_invalid_star2(self):
        with self.assertRaisesRegex(ValueError, "Stars must be a valid integer between 1 and 5."):
            self.manager.add_review(1, 0, "comment1")

    def test_invalid_star3(self):
        with self.assertRaisesRegex(ValueError, "Stars must be a valid integer between 1 and 5."):
            self.manager.add_review(1, 1.5, "comment1")

    def test_invalid_star4(self):
        with self.assertRaisesRegex(ValueError, "Stars must be a valid integer between 1 and 5."):
            self.manager.add_review(1, None, "comment1")

    def test_invalid_comment(self):
        with self.assertRaisesRegex(ValueError, "Comment must be a string."):
            self.manager.add_review(1, 5, 1)

    def test_invalid_comment1(self):
        with self.assertRaisesRegex(ValueError, "Comment must be a string."):
            self.manager.add_review(1, 5, None)

    def test_invalid_comment2(self):
        with self.assertRaisesRegex(ValueError, "Comment must be a string."):
            self.manager.add_review(1, 5, "")


class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        self.manager = Reviews()

    def test_get_nonexistent_review(self):
        self.assertIsNone(self.manager.get_review(999))

    def test_get_review_with_none_id(self):
        with self.assertRaisesRegex(TypeError, "Review ID must be a valid integer."):
            self.manager.get_review(None)

    def test_delete_nonexistent_review(self):
        with self.assertRaisesRegex(KeyError, "Review with this ID does not exist."):
            self.manager.delete_review(999)

    def test_edit_nonexistent_review(self):
        with self.assertRaisesRegex(KeyError, "Review with this ID does not exist."):
            self.manager.edit_review(999, 4, "new comment")

    def test_delete_review_with_none_id(self):
        with self.assertRaisesRegex(KeyError, "Review with this ID does not exist."):
            self.manager.delete_review(None)

    def test_edit_review_invalid_stars(self):
        self.manager.add_review(1, 5, "comment1")
        with self.assertRaisesRegex(ValueError, "Stars must be a valid integer between 1 and 5."):
            self.manager.edit_review(1, 6, "comment1")

    def test_edit_review_invalid_comment(self):
        self.manager.add_review(1, 5, "comment1")
        with self.assertRaisesRegex(ValueError, "Comment must be a string."):
            self.manager.edit_review(1, 4, None)

    def test_edit_review_with_none_id(self):
        with self.assertRaisesRegex(KeyError, "Review with this ID does not exist."):
            self.manager.edit_review(None, 4, "comment")


class TestReviewLifecycle(unittest.TestCase):
    def setUp(self):
        self.manager = Reviews()

    def test_full_review_lifecycle(self):
        # Add review
        self.manager.add_review(1, 5, "initial review")
        self.assertIsNotNone(self.manager.get_review(1))

        # Edit review
        self.manager.edit_review(1, 4, "updated review")
        updated_review = self.manager.get_review(1)
        self.assertEqual(updated_review.stars, 4)
        self.assertEqual(updated_review.comment, "updated review")

        # Delete review
        self.manager.delete_review(1)
        self.assertIsNone(self.manager.get_review(1))

    def test_review_edge_cases(self):
        # Test adding review with boundary star values
        self.manager.add_review(1, 1, "minimum stars")
        self.assertEqual(self.manager.get_review(1).stars, 1)

        self.manager.add_review(2, 5, "maximum stars")
        self.assertEqual(self.manager.get_review(2).stars, 5)

        # Test editing with boundary values
        self.manager.edit_review(1, 5, "updated to max")
        self.assertEqual(self.manager.get_review(1).stars, 5)

        self.manager.edit_review(2, 1, "updated to min")
        self.assertEqual(self.manager.get_review(2).stars, 1)


if __name__ == '__main__':
    unittest.main()
