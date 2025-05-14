import pytest
from src.users import UserManagement

@pytest.fixture
def manager():
    return UserManagement()

def test_addUser_email(manager):
    email = manager.addUser("user@mail.com", "password")
    assert manager.users[email].email == "user@mail.com"

def test_addUser_password(manager):
    passwd = manager.addUser("user@mail.com", "password")
    assert manager.users[passwd].password == "password"

def test_updateUser_email(manager):
    email = manager.addUser("user@mail.com", "password")
    manager.updateUser(email, "user@mail.com1")
    assert manager.users[email].email == "user@mail.com1"

def test_updateUser_password(manager):
    passwd = manager.addUser("user@mail.com", "password")
    manager.updateUser(passwd, "password1")
    assert manager.users[passwd].password == "password1"