"""
Moduł testów dla systemu rezerwacji.

Ten moduł zawiera testy jednostkowe sprawdzające poprawność działania
systemu rezerwacji, w tym tworzenie, anulowanie i zarządzanie rezerwacjami.
"""

import unittest
from src.reservation import ReservationManagement
from parameterized import parameterized


class TestBaseFunctions(unittest.TestCase):
    """
    Testy podstawowych funkcjonalności systemu rezerwacji.

    Sprawdza podstawowe operacje na rezerwacjach, takie jak:
    - tworzenie pojedynczych i wielu rezerwacji
    - rezerwacje dla różnych użytkowników
    - rezerwacje pokoi z różną liczbą łóżek
    - anulowanie rezerwacji
    """
    def setUp(self):
        """Przygotowuje środowisko testowe przed każdym testem."""
        self.manager = ReservationManagement()

    def test_booking_room_with_1_bed(self):
        """Sprawdza poprawność rezerwacji pokoju z jednym łóżkiem."""
        self.manager.booking(1, "user1", "2026-03-01", 1)
        self.assertEqual(self.manager.reservations[0].beds, 1)
        self.assertEqual(self.manager.reservations[0].user, "user1")
        self.assertEqual(self.manager.reservations[0].date, "2026-03-01")

    def test_booking_room_with_2_beds(self):
        self.manager.booking(1, "user1", "2026-03-01", 2)
        self.assertEqual(self.manager.reservations[0].beds, 2)
        self.assertEqual(self.manager.reservations[0].user, "user1")
        self.assertEqual(self.manager.reservations[0].date, "2026-03-01")

    def test_multiple_users_booking_multiple_rooms(self):
        self.manager.booking(1, "user1", "2026-03-01", 1)
        self.manager.booking(2, "user1", "2026-03-02", 2)
        self.manager.booking(3, "user1", "2026-03-02", 3)
        self.manager.booking(4, "user2", "2026-03-02", 2)
        self.manager.booking(5, "user2", "2026-03-03", 3)
        self.manager.booking(6, "user2", "2026-03-03", 4)
        self.manager.booking(7, "user3", "2026-03-03", 3)
        self.assertEqual(len(self.manager.reservations), 7)
        self.assertTrue(all(r.beds > 0 for r in self.manager.reservations))
        self.assertTrue(all(isinstance(r.user, str) for r in self.manager.reservations))
        self.assertTrue(all(isinstance(r.date, str) for r in self.manager.reservations))

    def test_user1_booking_room_with_multiple_beds(self):
        self.manager.booking(1, "user1", "2026-03-01", 2)
        self.manager.booking(2, "user1", "2026-03-02", 4)
        user_reservations = self.manager.userReservation(1)
        self.assertEqual(len(user_reservations), 1)
        user_reservations = self.manager.userReservation(2)
        self.assertEqual(len(user_reservations), 1)
        self.assertEqual(self.manager.reservations[0].beds, 2)
        self.assertEqual(self.manager.reservations[1].beds, 4)

    def test_booking_room_with_multiple_beds(self):
        self.manager.booking(1, "user1", "2026-03-01", 2)
        self.manager.booking(2, "user2", "2026-03-02", 4)
        self.assertEqual(len(self.manager.reservations), 2)
        self.assertEqual(self.manager.reservations[0].beds, 2)
        self.assertEqual(self.manager.reservations[1].beds, 4)

    def test_multiple_bookings(self):
        self.manager.booking(1, "user1", "2026-03-01", 1)
        self.manager.booking(1, "user1", "2026-03-02", 2)
        self.manager.booking(2, "user2", "2026-03-03", 3)
        self.manager.booking(3, "user3", "2026-03-04", 4)
        self.assertEqual(len(self.manager.userReservation(1)), 2)
        self.assertEqual(len(self.manager.userReservation(2)), 1)
        self.assertEqual(len(self.manager.userReservation(3)), 1)

    def test_cancel_booking(self):
        self.manager.booking(1, "user1", "2026-03-01", 1)
        self.assertTrue(self.manager.cancelBooking(1))
        self.assertEqual(len(self.manager.reservations), 0)

    def test_cancel_multiple_bookings(self):
        self.manager.booking(1, "user1", "2026-03-01", 1)
        self.manager.booking(2, "user1", "2026-03-02", 2)
        self.assertTrue(self.manager.cancelBooking(1))
        self.assertTrue(self.manager.cancelBooking(2))
        self.assertEqual(len(self.manager.reservations), 0)

    def test_userReservation(self):
        self.manager.booking(1, "user1", "2026-03-01", 1)
        reservations = self.manager.userReservation(1)
        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0].user, "user1")
        self.assertEqual(reservations[0].date, "2026-03-01")
        self.assertEqual(reservations[0].beds, 1)


class TestInvalidInputs(unittest.TestCase):
    """
    Testy walidacji niepoprawnych danych wejściowych.

    Sprawdza reakcję systemu na nieprawidłowe dane, w tym:
    - niepoprawne identyfikatory użytkowników
    - niepoprawne nazwy użytkowników
    - niepoprawne formaty dat
    - niepoprawne liczby łóżek
    """
    def setUp(self):
        """Przygotowuje środowisko testowe przed każdym testem."""
        self.manager = ReservationManagement()

    def test_valid_id(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.booking("invalid_id", "user1", "2026-03-01", 1)

    def test_valid_id1(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.booking(-1, "user1", "2026-03-01", 1)

    def test_valid_id2(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.booking(0, "user1", "2026-03-01", 1)

    def test_valid_id3(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.booking(1.5, "user1", "2026-03-01", 1)

    def test_valid_id4(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.booking("!@#$%", "user1", "2026-03-01", 1)

    def test_valid_username(self):
        with self.assertRaisesRegex(ValueError, "User name must be a valid string."):
            self.manager.booking(1, 1, "2026-03-01", 1)

    def test_valid_username1(self):
        with self.assertRaisesRegex(ValueError, "User name must contain only letters and numbers."):
            self.manager.booking(1, "user@name", "2026-03-01", 1)

    def test_valid_username2(self):
        with self.assertRaisesRegex(ValueError, "User name must contain only letters and numbers."):
            self.manager.booking(1, "!@#$%", "2026-03-01", 1)

    def test_valid_username3(self):
        with self.assertRaisesRegex(ValueError, "User name must contain only letters and numbers."):
            self.manager.booking(1, "user#$%", "2026-03-01", 1)

    def test_valid_date_format(self):
        with self.assertRaisesRegex(ValueError, "Date must be a valid string in 'YYYY-MM-DD' format."):
            self.manager.booking(1, "user1", "2026/03/01", 1)

    def test_valid_date_format2(self):
        with self.assertRaisesRegex(ValueError, "Date must be a valid string in 'YYYY-MM-DD' format."):
            self.manager.booking(1, "user1", "2026.03.01", 1)

    def test_valid_date_format3(self):
        with self.assertRaisesRegex(ValueError, "Date must be a valid string in 'YYYY-MM-DD' format."):
            self.manager.booking(1, "user1", "2026*03*01", 1)

    def test_valid_date_format4(self):
        with self.assertRaisesRegex(ValueError, "Date must be a valid string in 'YYYY-MM-DD' format."):
            self.manager.booking(1, "user1", "2026|03|01", 1)

    def test_valid_date_format5(self):
        with self.assertRaisesRegex(ValueError, "Date must be a valid string in 'YYYY-MM-DD' format."):
            self.manager.booking(1, "user1", "2026\\03\\01", 1)

    def test_valid_beds(self):
        with self.assertRaisesRegex(ValueError, "Number of beds must be a valid integer."):
            self.manager.booking(1, "user1", "2026-03-01", "1")

    def test_valid_beds1(self):
        with self.assertRaisesRegex(ValueError, "Number of beds must be a valid integer."):
            self.manager.booking(1, "user1", "2026-03-01", "1.5")

    def test_valid_beds2(self):
        with self.assertRaisesRegex(ValueError, "Number of beds must be a valid integer."):
            self.manager.booking(1, "user1", "2026-03-01", -1)

    def test_valid_beds3(self):
        with self.assertRaisesRegex(ValueError, "Number of beds must be a valid integer."):
            self.manager.booking(1, "user1", "2026-03-01", 0)

    def test_valid_beds_string(self):
        with self.assertRaisesRegex(ValueError, "Number of beds must be a valid integer."):
            self.manager.booking(1, "user1", "2026-03-01", "number")

    def test_valid_beds4(self):
        with self.assertRaisesRegex(ValueError, "Number of beds must be a valid integer."):
            self.manager.booking(1, "user1", "2026-03-01", 1.5)

    def test_valid_beds5(self):
        with self.assertRaisesRegex(ValueError, "Number of beds must be a valid integer."):
            self.manager.booking(1, "user1", "2026-03-01", -1.5)

    def test_valid_beds6(self):
        with self.assertRaisesRegex(ValueError, "Number of beds must be a valid integer."):
            self.manager.booking(1, "user1", "2026-03-01", "!@#$")


class TestReservationEdgeCases(unittest.TestCase):
    """
    Testy przypadków brzegowych systemu rezerwacji.

    Sprawdza zachowanie systemu w nietypowych sytuacjach, takich jak:
    - anulowanie nieistniejących rezerwacji
    - próba wielokrotnych rezerwacji
    - rezerwacje w tych samych terminach
    """
    def setUp(self):
        """Przygotowuje środowisko testowe przed każdym testem."""
        self.manager = ReservationManagement()

    def test_cancel_nonexistent_booking(self):
        self.assertFalse(self.manager.cancelBooking(999))

    def test_cancel_booking_verify_removal(self):
        self.manager.booking(1, "user1", "2026-03-01", 1)
        initial_count = len(self.manager.reservations)
        self.assertTrue(self.manager.cancelBooking(1))
        self.assertEqual(len(self.manager.reservations), initial_count - 1)

    def test_booking_different_users_same_date(self):
        self.manager.booking(1, "user1", "2026-03-01", 1)
        self.manager.booking(2, "user2", "2026-03-01", 1)
        self.assertEqual(len(self.manager.reservations), 2)

    def test_booking_same_user_same_date(self):
        self.manager.booking(1, "user1", "2026-03-01", 1)
        with self.assertRaisesRegex(ValueError, "User already booked room\\(s\\) on this date."):
            self.manager.booking(1, "user1", "2026-03-01", 2)


class TestReservationValidation(unittest.TestCase):
    """
    Testy walidacji danych rezerwacji.

    Sprawdza poprawność walidacji danych wejściowych, w tym:
    - obsługę wartości None
    - obsługę pustych ciągów znaków
    - obsługę niepoprawnych typów danych
    """
    def setUp(self):
        """Przygotowuje środowisko testowe przed każdym testem."""
        self.manager = ReservationManagement()

    def test_booking_none_date(self):
        with self.assertRaisesRegex(ValueError, "Date must be a valid string in 'YYYY-MM-DD' format."):
            self.manager.booking(1, "user1", None, 1)

    def test_booking_empty_date(self):
        with self.assertRaisesRegex(ValueError, "Date must be a valid string in 'YYYY-MM-DD' format."):
            self.manager.booking(1, "user1", "", 1)

    def test_booking_none_user(self):
        with self.assertRaisesRegex(ValueError, "User name must be a valid string."):
            self.manager.booking(1, None, "2026-03-01", 1)

    def test_booking_empty_user(self):
        with self.assertRaisesRegex(ValueError, "User name must be a valid string."):
            self.manager.booking(1, "", "2026-03-01", 1)

    def test_booking_none_beds(self):
        with self.assertRaisesRegex(ValueError, "Number of beds must be a valid integer."):
            self.manager.booking(1, "user1", "2026-03-01", None)


class TestUserReservationQueries(unittest.TestCase):
    """
    Testy zapytań o rezerwacje użytkowników.

    Sprawdza funkcjonalność związaną z pobieraniem informacji o rezerwacjach:
    - pobieranie rezerwacji dla konkretnego użytkownika
    - obsługa przypadku braku rezerwacji
    - obsługa przypadku po anulowaniu rezerwacji
    """
    def setUp(self):
        """Przygotowuje środowisko testowe przed każdym testem."""
        self.manager = ReservationManagement()

    def test_userReservation_invalid_id_type(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.userReservation("invalid")

    def test_userReservation_no_bookings(self):
        result = self.manager.userReservation(1)
        self.assertEqual(len(result), 0)

    def test_userReservation_multiple_dates(self):
        self.manager.booking(1, "user1", "2026-03-01", 1)
        self.manager.booking(1, "user1", "2026-03-02", 2)
        self.manager.booking(1, "user1", "2026-03-03", 3)
        result = self.manager.userReservation(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(r.user == "user1" for r in result))
        self.assertTrue(all(r.id == 1 for r in result))

    def test_userReservation_after_cancellation(self):
        self.manager.booking(1, "user1", "2026-03-01", 1)
        self.manager.booking(1, "user1", "2026-03-02", 2)
        self.assertTrue(self.manager.cancelBooking(1))
        result = self.manager.userReservation(1)
        self.assertEqual(len(result), 0)

    def test_userReservation_none_id(self):
        with self.assertRaisesRegex(ValueError, "User ID must be a valid integer."):
            self.manager.userReservation(None)


class TestParameterizedReservation(unittest.TestCase):
    """
    Klasa zawierająca parametryzowane testy dla systemu rezerwacji.
    
    Testy sprawdzają różne przypadki walidacji danych wejściowych oraz operacji na rezerwacjach
    przy użyciu parametryzacji.
    """
    
    def setUp(self):
        self.manager = ReservationManagement()

    @parameterized.expand([
        ("invalid_id_none", None, "user1", "2024-03-20", 2, "User ID must be a valid integer."),
        ("invalid_id_zero", 0, "user1", "2024-03-20", 2, "User ID must be a valid integer."),
        ("invalid_id_negative", -1, "user1", "2024-03-20", 2, "User ID must be a valid integer."),
        ("invalid_user_none", 1, None, "2024-03-20", 2, "User name must be a valid string."),
        ("invalid_user_empty", 1, "", "2024-03-20", 2, "User name must be a valid string."),
        ("invalid_user_special_chars", 1, "user@1", "2024-03-20", 2, "User name must contain only letters and numbers."),
        ("invalid_date_none", 1, "user1", None, 2, "Date must be a valid string in 'YYYY-MM-DD' format."),
        ("invalid_date_empty", 1, "user1", "", 2, "Date must be a valid string in 'YYYY-MM-DD' format."),
        ("invalid_date_format", 1, "user1", "20-03-2024", 2, "Date must be a valid string in 'YYYY-MM-DD' format."),
        ("invalid_beds_none", 1, "user1", "2024-03-20", None, "Number of beds must be a valid integer."),
        ("invalid_beds_zero", 1, "user1", "2024-03-20", 0, "Number of beds must be a valid integer."),
        ("invalid_beds_negative", 1, "user1", "2024-03-20", -1, "Number of beds must be a valid integer."),
    ])
    def test_booking_invalid_inputs(self, name, user_id, user, date, beds, expected_error):
        with self.assertRaisesRegex(ValueError, expected_error):
            self.manager.booking(user_id, user, date, beds)

    @parameterized.expand([
        ("single_bed", 1),
        ("double_bed", 2),
        ("family_room", 4),
        ("large_group", 8),
    ])
    def test_booking_different_bed_counts(self, name, beds):
        self.manager.booking(1, "user1", "2024-03-20", beds)
        reservations = self.manager.userReservation(1)
        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0].beds, beds)

    @parameterized.expand([
        ("past_date", "2023-01-01"),
        ("current_date", "2024-03-20"),
        ("future_date", "2024-12-31"),
    ])
    def test_booking_different_dates(self, name, date):
        self.manager.booking(1, "user1", date, 2)
        reservations = self.manager.userReservation(1)
        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0].date, date)

    @parameterized.expand([
        ("single_reservation", 1),
        ("few_reservations", 3),
        ("many_reservations", 5),
    ])
    def test_multiple_reservations(self, name, num_reservations):
        for i in range(num_reservations):
            self.manager.booking(1, "user1", f"2024-03-{20+i}", 2)
        reservations = self.manager.userReservation(1)
        self.assertEqual(len(reservations), num_reservations)


if __name__ == '__main__':
    unittest.main()
