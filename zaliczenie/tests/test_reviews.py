import pytest
from src.reviews import Reviews


@pytest.fixture
def manager():
    return Reviews()


class TestBaseFunctions:
    def test_add_review(self, manager):
        manager.add_review(1, 5, "comment1")
        assert manager.reviews_list[1].stars == 5

    def edit_review(self, manager):
        manager.add_review(1, 5, "comment1")
        manager.edit_review(1, 4, "comment2")
        assert manager.reviews_list[1].stars == 4

    def delete_review(self, manager):
        manager.add_review(1, 5, "comment1")
        manager.delete_review(1)
        assert len(manager.reviews_list) == 0
