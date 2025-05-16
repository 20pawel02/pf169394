import pytest
from src.users import UserManagement


@pytest.fixture
def manager():
    return UserManagement()


class TestBaseFunctions:
    def test_addUser_email(self, manager):
        email = manager.addUser("user@mail.com", "password123")
        assert manager.users[email].email == "user@mail.com"

    def test_addUser_password(self, manager):
        passwd = manager.addUser("user@mail.com", "password123")
        assert manager.users[passwd].password == "password123"

    def test_addUser_id_assignment(self, manager):
        user_id1 = manager.addUser("user1@mail.com", "password123")
        user_id2 = manager.addUser("user2@mail.com", "password123")
        assert user_id2 == user_id1 + 1

    def test_addUser_multiple(self, manager):
        manager.addUser("user1@mail.com", "password123")
        manager.addUser("user2@mail.com", "password123")
        manager.addUser("user3@mail.com", "password123")
        assert manager.getUser(2) is not None

    def test_getUser_existing(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        user = manager.getUser(user_id)
        assert user.email == "user@mail.com"
        assert user.password == "password123"

    def test_updateUser_email(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        manager.updateUser(user_id, "newemail@mail.com", "password123")
        assert manager.users[user_id].email == "newemail@mail.com"

    def test_updateUser_password(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        manager.updateUser(user_id, "user@mail.com", "newpassword123")
        assert manager.users[user_id].password == "newpassword123"

    def test_updateUser_both(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        manager.updateUser(user_id, "new@mail.com", "newpass123")
        assert manager.users[user_id].email == "new@mail.com"
        assert manager.users[user_id].password == "newpass123"

    def test_multiple_updates_same_user(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        manager.updateUser(user_id, "new1@mail.com", "password123")
        manager.updateUser(user_id, "new2@mail.com", "password123")
        manager.updateUser(user_id, "new3@mail.com", "password123")
        assert manager.getUser(user_id).email == "new3@mail.com"

    def test_deleteUser_success(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        manager.deleteUser(user_id)
        assert manager.getUser(user_id) is None

    def test_next_id_increment(self, manager):
        initial_next_id = manager.next_id
        manager.addUser("user1@mail.com", "password123")
        assert manager.next_id == initial_next_id + 1

    def test_next_id_after_deletion(self, manager):
        id1 = manager.addUser("user1@mail.com", "password123")
        initial_next_id = manager.next_id
        manager.deleteUser(id1)
        assert manager.next_id == initial_next_id

    def test_user_count(self, manager):
        initial_count = len(manager.users)
        manager.addUser("user1@mail.com", "password123")
        manager.addUser("user2@mail.com", "password123")
        assert len(manager.users) == initial_count + 2

    def test_user_count_after_deletion(self, manager):
        manager.addUser("user1@mail.com", "password123")
        manager.addUser("user2@mail.com", "password123")
        initial_count = len(manager.users)
        manager.deleteUser(1)
        assert len(manager.users) == initial_count - 1

    def test_add_update_delete_cycle(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        manager.updateUser(user_id, "new@mail.com", "newpass123")
        manager.deleteUser(user_id)
        assert manager.getUser(user_id) is None

    def test_multiple_users_operations(self, manager):
        id1 = manager.addUser("user1@mail.com", "password123")
        id2 = manager.addUser("user2@mail.com", "password123")
        id3 = manager.addUser("user3@mail.com", "password123")

        manager.updateUser(id2, "updated2@mail.com", "newpass123")
        manager.deleteUser(id1)

        assert manager.getUser(id1) is None
        assert manager.getUser(id2).email == "updated2@mail.com"
        assert manager.getUser(id3).email == "user3@mail.com"


class TestInvalidInputs:
    def test_addUser_empty_email(self, manager):
        with pytest.raises(ValueError, match="Email must be a valid string."):
            manager.addUser("", "password123")

    def test_addUser_none_email(self, manager):
        with pytest.raises(ValueError, match="Email must be a valid string."):
            manager.addUser(None, "password123")

    def test_addUser_invalid_email_type(self, manager):
        with pytest.raises(ValueError, match="Email must be a valid string."):
            manager.addUser(123, "password123")

    def test_addUser_duplicate_email(self, manager):
        manager.addUser("user@mail.com", "password123")
        with pytest.raises(ValueError, match="User already exists."):
            manager.addUser("user@mail.com", "different123")

    def test_addUser_short_password(self, manager):
        with pytest.raises(ValueError, match="Password must be longer than 8 characters."):
            manager.addUser("user@mail.com", "short")

    def test_addUser_empty_password(self, manager):
        with pytest.raises(ValueError, match="Password must be longer than 8 characters."):
            manager.addUser("user@mail.com", "")

    def test_addUser_none_password(self, manager):
        with pytest.raises(ValueError, match="Password must be longer than 8 characters."):
            manager.addUser("user@mail.com", None)

    def test_updateUser_nonexistent_user(self, manager):
        with pytest.raises(ValueError, match="User not exists."):
            manager.updateUser(999, "email@mail.com", "password123")

    def test_updateUser_empty_email(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        with pytest.raises(ValueError, match="Email must be a valid string."):
            manager.updateUser(user_id, "", "password123")

    def test_updateUser_none_email(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        with pytest.raises(ValueError, match="Email must be a valid string."):
            manager.updateUser(user_id, None, "password123")

    def test_updateUser_invalid_email_type(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        with pytest.raises(ValueError, match="Email must be a valid string."):
            manager.updateUser(user_id, 123, "password123")

    def test_updateUser_short_password(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        with pytest.raises(ValueError, match="Password must be longer than 8 characters."):
            manager.updateUser(user_id, "new@mail.com", "short")

    def test_updateUser_duplicate_email(self, manager):
        manager.addUser("user1@mail.com", "password123")
        user_id2 = manager.addUser("user2@mail.com", "password123")
        with pytest.raises(ValueError, match="Email already exists."):
            manager.updateUser(user_id2, "user1@mail.com", "password123")

    def test_deleteUser_nonexistent_user(self, manager):
        with pytest.raises(ValueError, match="User is not existing."):
            manager.deleteUser(999)

    def test_deleteUser_with_reservations(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        manager.users[user_id].reservations.append("some_reservation")
        with pytest.raises(ValueError, match="User have existing reservations."):
            manager.deleteUser(user_id)


class TestEdgeCases:
    def test_getUser_nonexistent(self, manager):
        assert manager.getUser(999) is None

    def test_update_user_same_email(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        manager.updateUser(user_id, "user@mail.com", "newpassword123")
        assert manager.users[user_id].email == "user@mail.com"
        assert manager.users[user_id].password == "newpassword123"

    def test_get_user_with_none_id(self, manager):
        assert manager.getUser(None) is None

    def test_get_user_with_zero_id(self, manager):
        assert manager.getUser(0) is None

    def test_get_user_with_negative_id(self, manager):
        assert manager.getUser(-1) is None

    def test_sequential_id_after_delete(self, manager):
        id1 = manager.addUser("user1@mail.com", "password123")
        manager.deleteUser(id1)
        id2 = manager.addUser("user2@mail.com", "password123")
        assert id2 == id1 + 1

    def test_update_after_other_user_deleted(self, manager):
        id1 = manager.addUser("user1@mail.com", "password123")
        id2 = manager.addUser("user2@mail.com", "password123")
        assert len(manager.users[id1].reservations) == 0
        manager.deleteUser(id1)
        manager.updateUser(id2, "updated2@mail.com", "newpassword123")
        assert manager.getUser(id2).email == "updated2@mail.com"
        assert manager.getUser(id2).password == "newpassword123"

    def test_add_delete_add_same_email(self, manager):
        id1 = manager.addUser("user@mail.com", "password123")
        manager.deleteUser(id1)
        id2 = manager.addUser("user@mail.com", "password123")
        assert id1 != id2

    def test_user_with_no_reservations(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        assert len(manager.users[user_id].reservations) == 0

    def test_delete_user_after_reservation_removal(self, manager):
        user_id = manager.addUser("user@mail.com", "password123")
        manager.users[user_id].reservations.append("reservation1")
        manager.users[user_id].reservations.pop()  # Remove the reservation
        manager.deleteUser(user_id)
