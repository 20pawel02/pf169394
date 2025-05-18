import unittest
from src.users import UserManagement
from parameterized import parameterized


class TestBaseFunctions(unittest.TestCase):
    """
    Klasa testująca podstawowe funkcjonalności użytkowników.

    Testuje przypadki poprawnego dodawania, aktualizowania i usuwania użytkowników.
    Dodatkowo sprawdza poprawną obsługę identyfikatorów użytkowników oraz liczbę użytkowników w systemie.
    """

    def setUp(self):
        self.manager = UserManagement()

    def test_addUser_email(self):
        user_id = self.manager.addUser("user@mail.com", "password123")
        self.assertEqual(self.manager.users[user_id].email, "user@mail.com")

    def test_addUser_password(self):
        user_id = self.manager.addUser("user@mail.com", "password123")
        self.assertEqual(self.manager.users[user_id].password, "password123")

    def test_addUser_id_assignment(self):
        user_id1 = self.manager.addUser("user1@mail.com", "password123")
        user_id2 = self.manager.addUser("user2@mail.com", "password123")
        self.assertEqual(user_id2, user_id1 + 1)

    def test_getUser_existing(self):
        user_id = self.manager.addUser("user@mail.com", "password123")
        user = self.manager.getUser(user_id)
        self.assertEqual(user.email, "user@mail.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(len(user.reservations), 0)

    def test_updateUser_email(self):
        # update email
        user_id = self.manager.addUser("user@mail.com", "password123")
        self.manager.updateUser(user_id, "newemail@mail.com", "password123")
        self.assertEqual(self.manager.users[user_id].email, "newemail@mail.com")

        # update password
        user_id = self.manager.addUser("user@mail.com", "password123")
        self.manager.updateUser(user_id, "user@mail.com", "newpassword123")
        self.assertEqual(self.manager.users[user_id].password, "newpassword123")

    def test_deleteUser_success(self):
        user_id = self.manager.addUser("user@mail.com", "password123")
        self.manager.deleteUser(user_id)
        self.assertIsNone(self.manager.getUser(user_id))


class TestInvalidInputs(unittest.TestCase):
    """
    Klasa testująca obsługę niepoprawnych danych wejściowych.

    Testuje przypadki niepoprawnego e-maila, hasła oraz obsługę brakujących danych.
    """

    def setUp(self):
        self.manager = UserManagement()

    def test_addUser_empty_email(self):
        with self.assertRaisesRegex(ValueError, "Email must be a valid string."):
            self.manager.addUser("", "password123")

        with self.assertRaisesRegex(ValueError, "Email must be a valid string."):
            self.manager.addUser(None, "password123")

        with self.assertRaisesRegex(ValueError, "Email must be a valid string."):
            self.manager.addUser(123, "password123")

    def test_addUser_password(self):
        with self.assertRaisesRegex(ValueError, "Password must be longer than 8 characters."):
            self.manager.addUser("user@mail.com", "short")

        with self.assertRaisesRegex(ValueError, "Password must be longer than 8 characters."):
            self.manager.addUser("user@mail.com", "")

        with self.assertRaisesRegex(ValueError, "Password must be longer than 8 characters."):
            self.manager.addUser("user@mail.com", None)

        user_id = self.manager.addUser("user1@mail.com", "password123")
        with self.assertRaisesRegex(ValueError, "Email must be a valid string."):
            self.manager.updateUser(user_id, None, "password123")

    def test_updateUser_short_password(self):
        user_id = self.manager.addUser("user@mail.com", "password123")
        with self.assertRaisesRegex(ValueError, "Password must be longer than 8 characters."):
            self.manager.updateUser(user_id, "new@mail.com", "short")


class TestEdgeCases(unittest.TestCase):
    """
    Klasa testująca przypadki brzegowe w systemie zarządzania użytkownikami.
    Testuje specyficzne sytuacje graniczne, takie jak:
    - Operacje na nieistniejących użytkownikach
    - Aktualizacje z tymi samymi danymi
    - Operacje z nieprawidłowymi identyfikatorami
    - Sekwencyjność identyfikatorów po usunięciu użytkowników
    - Interakcje między różnymi operacjami na użytkownikach
    """

    def setUp(self):
        self.manager = UserManagement()

    def test_getUser_nonexistent(self):
        self.assertIsNone(self.manager.getUser(999))

    def test_update_user_same_email(self):
        user_id = self.manager.addUser("user@mail.com", "password123")
        self.manager.updateUser(user_id, "user@mail.com", "newpassword123")
        self.assertEqual(self.manager.users[user_id].email, "user@mail.com")
        self.assertEqual(self.manager.users[user_id].password, "newpassword123")

    def test_get_user_with_none_id(self):
        self.assertIsNone(self.manager.getUser(None))

    def test_get_user_with_zero_id(self):
        self.assertIsNone(self.manager.getUser(0))

    def test_get_user_with_negative_id(self):
        self.assertIsNone(self.manager.getUser(-1))

    def test_sequential_id_after_delete(self):
        id1 = self.manager.addUser("user1@mail.com", "password123")
        self.manager.deleteUser(id1)
        id2 = self.manager.addUser("user2@mail.com", "password123")
        self.assertEqual(id2, id1 + 1)

    def test_update_after_other_user_deleted(self):
        id1 = self.manager.addUser("user1@mail.com", "password123")
        id2 = self.manager.addUser("user2@mail.com", "password123")
        self.assertEqual(len(self.manager.users[id1].reservations), 0)
        self.manager.deleteUser(id1)
        self.manager.updateUser(id2, "updated2@mail.com", "newpassword123")
        self.assertEqual(self.manager.getUser(id2).email, "updated2@mail.com")
        self.assertEqual(self.manager.getUser(id2).password, "newpassword123")

    def test_add_delete_add_same_email(self):
        id1 = self.manager.addUser("user@mail.com", "password123")
        self.manager.deleteUser(id1)
        id2 = self.manager.addUser("user@mail.com", "password123")
        self.assertNotEqual(id1, id2)

    def test_delete_user_after_reservation_removal(self):
        user_id = self.manager.addUser("user@mail.com", "password123")
        self.manager.users[user_id].reservations.append("some_reservation")
        self.manager.users[user_id].reservations.clear()
        self.manager.deleteUser(user_id)
        self.assertIsNone(self.manager.getUser(user_id))


class TestUserLifecycle(unittest.TestCase):
    """
    Klasa testująca pełny cykl życia użytkownika w systemie.

    Testuje kompletną ścieżkę użytkownika od utworzenia, przez aktualizacje,
    aż do usunięcia, weryfikując poprawność wszystkich operacji i walidacji
    na każdym etapie.
    """

    def setUp(self):
        self.manager = UserManagement()

    def test_full_user_lifecycle(self):
        # Add user
        user_id = self.manager.addUser("user@mail.com", "password123")
        self.assertIsNotNone(self.manager.getUser(user_id))
        self.assertEqual(self.manager.getUser(user_id).email, "user@mail.com")

        # Update user
        self.manager.updateUser(user_id, "updated@mail.com", "newpassword123")
        self.assertEqual(self.manager.getUser(user_id).email, "updated@mail.com")
        self.assertEqual(self.manager.getUser(user_id).password, "newpassword123")

        # Delete user
        self.manager.deleteUser(user_id)
        self.assertIsNone(self.manager.getUser(user_id))

    def test_update_user_validation(self):
        user_id = self.manager.addUser("user@mail.com", "password123")

        # Test updating with invalid email
        with self.assertRaisesRegex(ValueError, "Email must be a valid string."):
            self.manager.updateUser(user_id, "", "password123")

        # Test updating with invalid password
        with self.assertRaisesRegex(ValueError, "Password must be longer than 8 characters."):
            self.manager.updateUser(user_id, "new@mail.com", "short")

    def test_delete_user_validation(self):
        # Test deleting non-existent user
        with self.assertRaisesRegex(ValueError, "User is not existing."):
            self.manager.deleteUser(999)

        # Test deleting user with reservations
        user_id = self.manager.addUser("user@mail.com", "password123")
        self.manager.users[user_id].reservations.append("some_reservation")
        with self.assertRaisesRegex(ValueError, "User have existing reservations."):
            self.manager.deleteUser(user_id)


class TestReservationIntegration(unittest.TestCase):
    """
    Klasa testująca integrację między systemem użytkowników a rezerwacjami.

    Sprawdza poprawność interakcji między użytkownikami a ich rezerwacjami,
    w tym wpływ rezerwacji na możliwość usuwania użytkowników oraz
    poprawność powiązań między obiektami.
    """

    def setUp(self):
        self.manager = UserManagement()

    def test_user_with_reservations(self):
        user_id = self.manager.addUser("user@mail.com", "password123")
        self.manager.users[user_id].reservations.append("reservation1")
        self.manager.users[user_id].reservations.append("reservation2")

        # Try to delete user with reservations
        with self.assertRaisesRegex(ValueError, "User have existing reservations."):
            self.manager.deleteUser(user_id)

        # Remove reservations and try again
        self.manager.users[user_id].reservations.clear()
        self.manager.deleteUser(user_id)
        self.assertIsNone(self.manager.getUser(user_id))


class TestParameterized(unittest.TestCase):
    """
    Klasa zawierająca parametryzowane testy dla systemu zarządzania użytkownikami.
    Testy sprawdzają różne przypadki walidacji danych wejściowych oraz operacji na użytkownikach
    przy użyciu parametryzacji, co pozwala na bardziej zwięzłe i czytelne testy.
    """

    def setUp(self):
        self.manager = UserManagement()

    @parameterized.expand([
        ("empty_email", "", "password123", "Email must be a valid string."),
        ("none_email", None, "password123", "Email must be a valid string."),
        ("numeric_email", 123, "password123", "Email must be a valid string."),
        ("empty_password", "user@mail.com", "", "Password must be longer than 8 characters."),
        ("none_password", "user@mail.com", None, "Password must be longer than 8 characters."),
        ("short_password", "user@mail.com", "short", "Password must be longer than 8 characters."),
    ])
    def test_addUser_invalid_inputs(self, name, email, password, expected_error):
        with self.assertRaisesRegex(ValueError, expected_error):
            self.manager.addUser(email, password)

    @parameterized.expand([
        ("empty_email", "", "newpass123"),
        ("none_email", None, "newpass123"),
        ("numeric_email", 123, "newpass123"),
    ])
    def test_updateUser_invalid_email(self, name, email, password):
        user_id = self.manager.addUser("user@mail.com", "password123")
        with self.assertRaisesRegex(ValueError, "Email must be a valid string."):
            self.manager.updateUser(user_id, email, password)

    @parameterized.expand([
        ("empty_password", "new@mail.com", ""),
        ("none_password", "new@mail.com", None),
        ("short_password", "new@mail.com", "short"),
    ])
    def test_updateUser_invalid_password(self, name, email, password):
        user_id = self.manager.addUser("user@mail.com", "password123")
        with self.assertRaisesRegex(ValueError, "Password must be longer than 8 characters."):
            self.manager.updateUser(user_id, email, password)

    @parameterized.expand([
        ("none_id", None),
        ("zero_id", 0),
        ("negative_id", -1),
        ("non_existent_id", 999),
    ])
    def test_getUser_invalid_ids(self, name, user_id):
        self.assertIsNone(self.manager.getUser(user_id))

    @parameterized.expand([
        ("single_reservation", ["reservation1"]),
        ("multiple_reservations", ["reservation1", "reservation2"]),
        ("many_reservations", ["r1", "r2", "r3", "r4", "r5"]),
    ])
    def test_deleteUser_with_different_reservations(self, name, reservations):
        user_id = self.manager.addUser("user@mail.com", "password123")
        for reservation in reservations:
            self.manager.users[user_id].reservations.append(reservation)
        with self.assertRaisesRegex(ValueError, "User have existing reservations."):
            self.manager.deleteUser(user_id)


if __name__ == '__main__':
    unittest.main()
