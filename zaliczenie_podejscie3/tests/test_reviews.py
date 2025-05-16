import pytest
from src.reviews import Reviews


@pytest.fixture
def manager():
    return Reviews()


class TestBaseFunctions:
    def test_add_review(self, manager):
        manager.add_review(1, 5, "comment1")
        assert manager.reviews_list[1].stars == 5

    def test_edit_review(self, manager):
        manager.add_review(1, 5, "comment1")
        manager.edit_review(1, 4, "comment1")
        assert manager.reviews_list[1].stars == 4

    def test_delete_review(self, manager):
        manager.add_review(1, 5, "comment1")
        manager.delete_review(1)
        assert len(manager.reviews_list) == 0

    def test_get_reviews(self, manager):
        manager.add_review(1, 5, "comment1")
        review = manager.get_review(1)
        assert review.id == 1
        assert review.stars == 5
        assert review.comment == "comment1"

        # Test getting a non-existent review
        assert manager.get_review(999) is None


class TestInvalidInputs:
    def test_invalid_id(self, manager):
        with pytest.raises(ValueError, match="User ID must be a valid integer."):
            manager.add_review("invalid", 5, "comment1")

    def test_invalid_id1(self, manager):
        with pytest.raises(ValueError, match="User ID must be a valid integer."):
            manager.add_review(-1, 5, "comment1")

    def test_invalid_id2(self, manager):
        with pytest.raises(ValueError, match="User ID must be a valid integer."):
            manager.add_review(0, 5, "comment1")

    def test_invalid_star(self, manager):
        with pytest.raises(ValueError, match="Stars must be a valid integer between 1 and 5."):
            manager.add_review(1, 6, "comment1")

    def test_invalid_star1(self, manager):
        with pytest.raises(ValueError, match="Stars must be a valid integer between 1 and 5."):
            manager.add_review(1, -1, "comment1")

    def test_invalid_star2(self, manager):
        with pytest.raises(ValueError, match="Stars must be a valid integer between 1 and 5."):
            manager.add_review(1, 0, "comment1")