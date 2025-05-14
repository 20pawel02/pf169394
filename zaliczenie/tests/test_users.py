import pytest
from src.users import UserManagement


@pytest.fixture
def manager():
    return UserManagement()


def test_addUser_email(manager):
    email = manager.addUser("user@mail.com", "password123")
    assert manager.users[email].email == "user@mail.com"


def test_addUser_password(manager):
    passwd = manager.addUser("user@mail.com", "password123")
    assert manager.users[passwd].password == "password123"


def test_addUser_id_assignment(manager):
    user_id1 = manager.addUser("user1@mail.com", "password123")
    user_id2 = manager.addUser("user2@mail.com", "password123")
    assert user_id2 == user_id1 + 1


def test_addUser_multiple(manager):
    manager.addUser("user1", "password")
    manager.addUser("user2", "password")
    manager.addUser("user3", "password")
    assert manager.getUser(2)  # collecting users id (id: 2 in this case)


def test_addUser_empty_email(manager):
    with pytest.raises(ValueError, match="Email must be a valid string."):
        manager.addUser("", "password123")


def test_addUser_none_email(manager):
    with pytest.raises(ValueError, match="Email must be a valid string."):
        manager.addUser(None, "password123")


def test_addUser_invalid_email_type(manager):
    with pytest.raises(ValueError, match="Email must be a valid string."):
        manager.addUser(123, "password123")


def test_addUser_duplicate_email(manager):
    manager.addUser("user@mail.com", "password123")
    with pytest.raises(ValueError, match="User already exists."):
        manager.addUser("user@mail.com", "different123")


def test_addUser_short_password(manager):
    with pytest.raises(ValueError, match="Password must be longer than 8 characters."):
        manager.addUser("user@mail.com", "short")


def test_addUser_empty_password(manager):
    with pytest.raises(ValueError, match="Password must be longer than 8 characters."):
        manager.addUser("user@mail.com", "")


def test_addUser_none_password(manager):
    with pytest.raises(ValueError, match="Password must be longer than 8 characters."):
        manager.addUser("user@mail.com", None)


def test_updateUser_email(manager):
    user_id = manager.addUser("user@mail.com", "password")
    manager.updateUser(user_id, "newemail@mail.com", "password")
    assert manager.users[user_id].email == "newemail@mail.com"


def test_updateUser_password(manager):
    user_id = manager.addUser("user@mail.com", "password123")
    manager.updateUser(user_id, "user@mail.com", "newpassword123")
    assert manager.users[user_id].password == "newpassword123"


def test_updateUser_both(manager):
    user_id = manager.addUser("user@mail.com", "password123")
    manager.updateUser(user_id, "new@mail.com", "newpass123")
    assert manager.users[user_id].email == "new@mail.com"
    assert manager.users[user_id].password == "newpass123"


def test_updateUser_nonexistent_user(manager):
    with pytest.raises(ValueError, match="User not exists."):
        manager.updateUser(999, "email@mail.com", "password123")


def test_updateUser_empty_email(manager):
    user_id = manager.addUser("user@mail.com", "password123")
    with pytest.raises(ValueError, match="Email must be a valid string."):
        manager.updateUser(user_id, "", "password123")


def test_updateUser_none_email(manager):
    user_id = manager.addUser("user@mail.com", "password123")
    with pytest.raises(ValueError, match="Email must be a valid string."):
        manager.updateUser(user_id, None, "password123")


def test_updateUser_invalid_email_type(manager):
    user_id = manager.addUser("user@mail.com", "password123")
    with pytest.raises(ValueError, match="Email must be a valid string."):
        manager.updateUser(user_id, 123, "password123")


def test_updateUser_short_password(manager):
    user_id = manager.addUser("user@mail.com", "password123")
    with pytest.raises(ValueError, match="Password must be longer than 8 characters."):
        manager.updateUser(user_id, "new@mail.com", "short")


def test_updateUser_duplicate_email(manager):
    manager.addUser("user1@mail.com", "password123")
    user_id2 = manager.addUser("user2@mail.com", "password123")
    with pytest.raises(ValueError, match="Email already exists."):
        manager.updateUser(user_id2, "user1@mail.com", "password123")


def test_deleteUser_success(manager):
    user_id = manager.addUser("user@mail.com", "password123")
    manager.deleteUser(user_id)
    assert manager.getUser(user_id) is None


def test_deleteUser_nonexistent_user(manager):
    with pytest.raises(ValueError, match="User is not existing."):
        manager.deleteUser(999)


def test_deleteUser_with_reservations(manager):
    user_id = manager.addUser("user@mail.com", "password123")
    manager.users[user_id].reservations.append("some_reservation")
    with pytest.raises(ValueError, match="User have existing reservations."):
        manager.deleteUser(user_id)


def test_getUser_existing(manager):
    user_id = manager.addUser("user@mail.com", "password123")
    user = manager.getUser(user_id)
    assert user.email == "user@mail.com"
    assert user.password == "password123"


def test_getUser_nonexistent(manager):
    assert manager.getUser(999) is None


def test_add_update_delete_cycle(manager):
    user_id = manager.addUser("user@mail.com", "password123")
    manager.updateUser(user_id, "new@mail.com", "newpass123")
    manager.deleteUser(user_id)
    assert manager.getUser(user_id) is None


def test_multiple_users_operations(manager):
    id1 = manager.addUser("user1@mail.com", "password123")
    id2 = manager.addUser("user2@mail.com", "password123")
    id3 = manager.addUser("user3@mail.com", "password123")

    manager.updateUser(id2, "updated2@mail.com", "newpass123")
    manager.deleteUser(id1)

    assert manager.getUser(id1) is None
    assert manager.getUser(id2).email == "updated2@mail.com"
    assert manager.getUser(id3).email == "user3@mail.com"


# Edge cases
def test_sequential_id_after_delete(manager):
    id1 = manager.addUser("user1@mail.com", "password123")
    manager.deleteUser(id1)
    id2 = manager.addUser("user2@mail.com", "password123")
    assert id2 == id1 + 1


def test_update_after_other_user_deleted(manager):
    id1 = manager.addUser("user1@mail.com", "password123")
    id2 = manager.addUser("user2@mail.com", "password123")

    # Make sure user1 has no reservations before deletion
    assert len(manager.users[id1].reservations) == 0

    # Delete first user
    manager.deleteUser(id1)

    # Update second user
    manager.updateUser(id2, "updated2@mail.com", "newpassword123")

    # Verify the update was successful
    assert manager.getUser(id2).email == "updated2@mail.com"
    assert manager.getUser(id2).password == "newpassword123"


def test_multiple_updates_same_user(manager):
    user_id = manager.addUser("user@mail.com", "password123")
    manager.updateUser(user_id, "new1@mail.com", "password123")
    manager.updateUser(user_id, "new2@mail.com", "password123")
    manager.updateUser(user_id, "new3@mail.com", "password123")
    assert manager.getUser(user_id).email == "new3@mail.com"


def test_add_delete_add_same_email(manager):
    id1 = manager.addUser("user@mail.com", "password123")
    manager.deleteUser(id1)
    id2 = manager.addUser("user@mail.com", "password123")
    assert id1 != id2


def test_complex_user_scenario(manager):
    id1 = manager.addUser("user1@mail.com", "password123")
    id2 = manager.addUser("user2@mail.com", "password123")

    manager.updateUser(id1, "updated1@mail.com", "newpass123")
    manager.deleteUser(id2)

    id3 = manager.addUser("user3@mail.com", "password123")
    manager.updateUser(id1, "final1@mail.com", "finalpass123")

    assert manager.getUser(id1).email == "final1@mail.com"
    assert manager.getUser(id2) is None
    assert manager.getUser(id3).email == "user3@mail.com"


def test_updateUser_password(manager):
    user_id = manager.addUser("user@mail.com", "password")
    manager.updateUser(user_id, "user@mail.com", "newpassword")
    assert manager.users[user_id].password == "newpassword"


def test_updateUser_password_and_email(manager):
    user_id = manager.addUser("user@mail.com", "password")
    manager.updateUser(user_id, "newemail@mail.com", "newpassword")
    assert manager.users[user_id].email == "newemail@mail.com"
    assert manager.users[user_id].password == "newpassword"
