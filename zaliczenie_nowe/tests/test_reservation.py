import unittest
from src.reservation import ReservationManagement


class TestBaseFunctions(unittest.TestCase):
    def setUp(self):
        self.manager = ReservationManagement()

    def test_booking_room_with_1_bed(self):
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
    def setUp(self):
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
    def setUp(self):
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
    def setUp(self):
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
    def setUp(self):
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


if __name__ == '__main__':
    unittest.main()
