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

    def test_invalid_id3(self, manager):
        with pytest.raises(ValueError, match="User ID must be a valid integer."):
            manager.add_review(1.5, 5, "comment1")

    def test_invalid_id4(self, manager):
        with pytest.raises(ValueError, match="User ID must be a valid integer."):
            manager.add_review(None, 5, "comment1")

    def test_invalid_star(self, manager):
        with pytest.raises(ValueError, match="Stars must be a valid integer between 1 and 5."):
            manager.add_review(1, 6, "comment1")

    def test_invalid_star1(self, manager):
        with pytest.raises(ValueError, match="Stars must be a valid integer between 1 and 5."):
            manager.add_review(1, -1, "comment1")

    def test_invalid_star2(self, manager):
        with pytest.raises(ValueError, match="Stars must be a valid integer between 1 and 5."):
            manager.add_review(1, 0, "comment1")

    def test_invalid_star3(self, manager):
        with pytest.raises(ValueError, match="Stars must be a valid integer between 1 and 5."):
            manager.add_review(1, 1.5, "comment1")

    def test_invalid_star4(self, manager):
        with pytest.raises(ValueError, match="Stars must be a valid integer between 1 and 5."):
            manager.add_review(1, None, "comment1")

    def test_invalid_comment(self, manager):
        with pytest.raises(ValueError, match="Comment must be a string."):
            manager.add_review(1, 5, 1)

    def test_invalid_comment1(self, manager):
        with pytest.raises(ValueError, match="Comment must be a string."):
            manager.add_review(1, 5, None)

    def test_invalid_comment2(self, manager):
        with pytest.raises(ValueError, match="Comment can be max 10 characters long."):
            manager.add_review(1, 5, "12345678901")


class TestEdgeCases:
    def test_get_nonexistent_review(self, manager):
        assert manager.get_review(999) is None
        
    def test_delete_nonexistent_review(self, manager):
        manager.delete_review(999)
        assert 999 not in manager.reviews_list
        
    def test_edit_nonexistent_review(self, manager):
        # Should not raise an error or modify anything
        manager.edit_review(999, 4, "new comment")
        assert 999 not in manager.reviews_list