"""
Moduł testów dla systemu recenzji.

Ten moduł zawiera testy jednostkowe sprawdzające poprawność działania
systemu recenzji, w tym dodawanie, edycję, usuwanie i pobieranie recenzji.
"""

import unittest
from src.reviews import Reviews
from parameterized import parameterized


class TestBaseFunctions(unittest.TestCase):
    """
    Testy podstawowych funkcjonalności systemu recenzji.

    Sprawdza podstawowe operacje na recenzjach, takie jak:
    - dodawanie pojedynczych i wielu recenzji
    - edycja istniejących recenzji
    - usuwanie recenzji
    - pobieranie recenzji
    """

    def setUp(self):
        """Przygotowuje środowisko testowe przed każdym testem."""
        self.manager = Reviews()

    def test_add_review(self):
        """Sprawdza poprawność dodawania nowej recenzji."""
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
    Testy walidacji niepoprawnych danych wejściowych.

    Sprawdza reakcję systemu na nieprawidłowe dane, w tym:
    - niepoprawne identyfikatory recenzji
    - niepoprawne oceny gwiazdkowe
    - niepoprawne komentarze
    - niepoprawne typy danych

    Te testy zapewniają, że system odpowiednio waliduje dane wejściowe
    i zgłasza odpowiednie wyjątki w przypadku błędnych danych.
    """

    def setUp(self):
        """Przygotowuje środowisko testowe przed każdym testem."""
        self.manager = Reviews()

    def test_invalid_id(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.add_review("invalid", 5, "comment1")

        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.add_review(-1, 5, "comment1")

        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.add_review(0, 5, "comment1")

        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.add_review(1.5, 5, "comment1")

        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.add_review(None, 5, "comment1")

    def test_invalid_star(self):
        with self.assertRaisesRegex(ValueError, "Stars must be a valid integer between 1 and 5."):
            self.manager.add_review(1, 6, "comment1")

    def test_invalid_star1(self):
        with self.assertRaisesRegex(ValueError, "Stars must be a valid integer between 1 and 5."):
            self.manager.add_review(1, -1, "comment1")

        with self.assertRaisesRegex(ValueError, "Stars must be a valid integer between 1 and 5."):
            self.manager.add_review(1, 0, "comment1")

        with self.assertRaisesRegex(ValueError, "Stars must be a valid integer between 1 and 5."):
            self.manager.add_review(1, 1.5, "comment1")

        with self.assertRaisesRegex(ValueError, "Stars must be a valid integer between 1 and 5."):
            self.manager.add_review(1, None, "comment1")

    def test_invalid_comment(self):
        with self.assertRaisesRegex(ValueError, "Comment must be a string."):
            self.manager.add_review(1, 5, 1)

        with self.assertRaisesRegex(ValueError, "Comment must be a string."):
            self.manager.add_review(1, 5, None)

        with self.assertRaisesRegex(ValueError, "Comment must be a string."):
            self.manager.add_review(1, 5, "")


class TestEdgeCases(unittest.TestCase):
    """
    Testy przypadków brzegowych systemu recenzji.

    Sprawdza zachowanie systemu w nietypowych sytuacjach, takich jak:
    - próba pobrania nieistniejącej recenzji
    - próba edycji nieistniejącej recenzji
    - próba usunięcia nieistniejącej recenzji
    - obsługa wartości granicznych dla ocen
    """

    def setUp(self):
        """Przygotowuje środowisko testowe przed każdym testem."""
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
    """
    Testy pełnego cyklu życia recenzji.

    Sprawdza kompletny proces zarządzania recenzją, w tym:
    - utworzenie nowej recenzji
    - edycję istniejącej recenzji
    - usunięcie recenzji
    - obsługę wartości granicznych dla ocen (1-5 gwiazdek)
    """

    def setUp(self):
        """Przygotowuje środowisko testowe przed każdym testem."""
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


class TestParameterizedReviews(unittest.TestCase):
    """
    Klasa zawierająca parametryzowane testy dla systemu recenzji.
    
    Testy sprawdzają różne przypadki walidacji danych wejściowych oraz operacji na recenzjach
    przy użyciu parametryzacji.
    """

    def setUp(self):
        self.reviews = Reviews()

    @parameterized.expand([
        ("invalid_id_none", None, 5, "Good review", "User ID must be a valid integer."),
        ("invalid_id_zero", 0, 5, "Good review", "User ID must be a valid integer."),
        ("invalid_id_negative", -1, 5, "Good review", "User ID must be a valid integer."),
        ("invalid_stars_none", 1, None, "Good review", "Stars must be a valid integer between 1 and 5."),
        ("invalid_stars_zero", 1, 0, "Good review", "Stars must be a valid integer between 1 and 5."),
        ("invalid_stars_negative", 1, -1, "Good review", "Stars must be a valid integer between 1 and 5."),
        ("invalid_stars_too_high", 1, 6, "Good review", "Stars must be a valid integer between 1 and 5."),
        ("invalid_comment_none", 1, 5, None, "Comment must be a string."),
        ("invalid_comment_empty", 1, 5, "", "Comment must be a string."),
    ])
    def test_add_review_invalid_inputs(self, name, user_id, stars, comment, expected_error):
        with self.assertRaisesRegex(ValueError, expected_error):
            self.reviews.add_review(user_id, stars, comment)

    @parameterized.expand([
        ("valid_stars_min", 1),
        ("valid_stars_mid", 3),
        ("valid_stars_max", 5),
    ])
    def test_add_review_valid_stars(self, name, stars):
        self.reviews.add_review(1, stars, "Good review")
        review = self.reviews.get_review(1)
        self.assertEqual(review.stars, stars)

    @parameterized.expand([
        ("short_comment", "OK"),
        ("medium_comment", "This was a good experience"),
        ("long_comment",
         "This was an excellent experience with great service and I would definitely recommend it to others!"),
    ])
    def test_add_review_different_comments(self, name, comment):
        self.reviews.add_review(1, 5, comment)
        review = self.reviews.get_review(1)
        self.assertEqual(review.comment, comment)

    @parameterized.expand([
        ("update_stars", 1, 4, "Original comment"),
        ("update_comment", 1, 5, "Updated comment"),
        ("update_both", 1, 3, "Both updated"),
    ])
    def test_edit_review_variations(self, name, user_id, new_stars, new_comment):
        # Add initial review
        self.reviews.add_review(user_id, 5, "Initial comment")
        # Edit review
        self.reviews.edit_review(user_id, new_stars, new_comment)
        # Verify changes
        review = self.reviews.get_review(user_id)
        self.assertEqual(review.stars, new_stars)
        self.assertEqual(review.comment, new_comment)


if __name__ == '__main__':
    unittest.main()
