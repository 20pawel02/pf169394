import pytest
from src.reservation import ReservationManagement


@pytest.fixture
def manager():
    """
    Fixture to create a fresh ReservationManagement instance for each test.

    Returns:
        ReservationManagement: A new reservation management instance.
    """
    return ReservationManagement()


class TestBaseFunctions:
    """
    Test suite for basic reservation management functionality.

    These tests verify core booking operations like single and multiple room bookings,
    and checking reservation details.
    """

    def test_booking_room_with_1_bed(self, manager):
        manager.booking(1, "user1", "2026-03-01", 1)
        assert manager.reservations[0].beds == 1

    def test_booking_room_with_2_beds(self, manager):
        manager.booking(1, "user1", "2026-03-01", 2)
        assert manager.reservations[0].beds == 2

    def test_multiple_users_booking_multiple_rooms(self, manager):
        manager.booking(1, "user1", "2026-03-01", 1)
        manager.booking(2, "user1", "2026-03-02", 2)
        manager.booking(3, "user1", "2026-03-02", 3)
        manager.booking(4, "user2", "2026-03-02", 2)
        manager.booking(5, "user2", "2026-03-03", 3)
        manager.booking(6, "user2", "2026-03-03", 4)
        manager.booking(7, "user3", "2026-03-03", 3)
        assert len(manager.reservations) == 7

    def test_user1_booking_room_with_multiple_beds(self, manager):
        manager.booking(1, "user1", "2026-03-01", 2)
        manager.booking(2, "user1", "2026-03-02", 4)
        user_reservations = manager.userReservation(1)
        assert len(user_reservations) == 1
        user_reservations = manager.userReservation(2)
        assert len(user_reservations) == 1
        assert manager.reservations[0].beds == 2
        assert manager.reservations[1].beds == 4

    def test_booking_room_with_multiple_beds(self, manager):
        manager.booking(1, "user1", "2026-03-01", 2)
        manager.booking(2, "user2", "2026-03-02", 4)
        assert len(manager.reservations) == 2
        assert manager.reservations[0].beds == 2
        assert manager.reservations[1].beds == 4

    def test_multiple_bookings(self, manager):
        manager.booking(1, "user1", "2026-03-01", 1)
        manager.booking(1, "user1", "2026-03-02", 2)
        manager.booking(2, "user2", "2026-03-03", 3)
        manager.booking(3, "user3", "2026-03-04", 4)
        assert len(manager.userReservation(1)) == 2
        assert len(manager.userReservation(2)) == 1
        assert len(manager.userReservation(3)) == 1

    def test_cancel_booking(self, manager):
        manager.booking(1, "user1", "2026-03-01", 1)
        manager.cancelBooking(1)
        assert len(manager.reservations) == 0

    def test_cancel_multiple_bookings(self, manager):
        manager.booking(1, "user1", "2026-03-01", 1)
        manager.booking(2, "user1", "2026-03-02", 2)
        manager.cancelBooking(1)
        manager.cancelBooking(2)
        assert len(manager.reservations) == 0

    def test_userReservation(self, manager):
        manager.booking(1, "user1", "2026-03-01", 1)
        assert manager.userReservation(1)

    def test_userReservation_no_bookings(self, manager):
        result = manager.userReservation(1)
        assert len(result) == 0

    def test_userReservation_multiple_dates(self, manager):
        manager.booking(1, "user1", "2026-03-01", 1)
        manager.booking(1, "user1", "2026-03-02", 2)
        manager.booking(1, "user1", "2026-03-03", 3)
        result = manager.userReservation(1)
        assert len(result) == 3
        assert all(r.user == "user1" for r in result)

    def test_userReservation_after_cancellation(self, manager):
        manager.booking(1, "user1", "2026-03-01", 1)
        manager.booking(1, "user1", "2026-03-02", 2)
        manager.cancelBooking(1)
        result = manager.userReservation(1)
        assert len(result) == 1


class TestInvalidInputs:
    """
    Test suite for input validation in reservation management.

    These tests ensure that the reservation system correctly handles
    various invalid input scenarios, such as incorrect user IDs, usernames,
    dates, and bed numbers.
    """

    def test_valid_id(self, manager):
        with pytest.raises(ValueError, match="User ID must be a valid integer."):
            manager.booking("invalid_id", "user1", "2026-03-01", 1)

    def test_valid_id1(self, manager):
        with pytest.raises(ValueError, match="User ID must be a valid integer."):
            manager.booking(-1, "user1", "2026-03-01", 1)

    def test_valid_id2(self, manager):
        with pytest.raises(ValueError, match="User ID must be a valid integer."):
            manager.booking(0, "user1", "2026-03-01", 1)

    def test_valid_id3(self, manager):
        with pytest.raises(ValueError, match="User ID must be a valid integer."):
            manager.booking(1.5, "user1", "2026-03-01", 1)

    def test_valid_id4(self, manager):
        with pytest.raises(ValueError, match="User ID must be a valid integer."):
            manager.booking(None, "user1", "2026-03-01", 1)

    def test_userReservation_invalid_id_type(self, manager):
        with pytest.raises(ValueError, match="User ID must be a valid integer."):
            manager.userReservation("invalid")

    def test_valid_username(self, manager):
        with pytest.raises(ValueError, match="User name must be a valid string."):
            manager.booking(1, 1, "2026-03-01", 1)

    def test_valid_username1(self, manager):
        with pytest.raises(
                ValueError, match="User name must contain only letters and numbers."
        ):
            manager.booking(1, "user@name", "2026-03-01", 1)

    def test_valid_username2(self, manager):
        with pytest.raises(ValueError, match="User name must be a valid string."):
            manager.booking(1, None, "2026-03-01", 1)

    def test_valid_username3(self, manager):
        with pytest.raises(ValueError, match="User name must be a valid string."):
            manager.booking(1, "", "2026-03-01", 1)

    def test_invalid_date(self, manager):
        with pytest.raises(
                ValueError, match="Date must be a valid string in 'YYYY-MM-DD' format."
        ):
            manager.booking(1, "user1", None, 1)

    def test_valid_date_format(self, manager):
        with pytest.raises(
                ValueError, match="Date must be a valid string in 'YYYY-MM-DD' format."
        ):
            manager.booking(1, "user1", "2026/03/01", 1)

    def test_valid_date_format2(self, manager):
        with pytest.raises(
                ValueError, match="Date must be a valid string in 'YYYY-MM-DD' format."
        ):
            manager.booking(1, "user1", "2026.03.01", 1)

    def test_valid_date_format3(self, manager):
        with pytest.raises(
                ValueError, match="Date must be a valid string in 'YYYY-MM-DD' format."
        ):
            manager.booking(1, "user1", "2026*03*01", 1)

    def test_valid_date_format4(self, manager):
        with pytest.raises(
                ValueError, match="Date must be a valid string in 'YYYY-MM-DD' format."
        ):
            manager.booking(1, "user1", "2026|03|01", 1)

    def test_valid_date_format5(self, manager):
        with pytest.raises(
                ValueError, match="Date must be a valid string in 'YYYY-MM-DD' format."
        ):
            manager.booking(1, "user1", "2026\03\01", 1)

    def test_valid_beds(self, manager):
        with pytest.raises(ValueError, match="Number of beds must be a valid integer."):
            manager.booking(1, "user1", "2026-03-01", "1")

    def test_valid_beds1(self, manager):
        with pytest.raises(ValueError, match="Number of beds must be a valid integer."):
            manager.booking(1, "user1", "2026-03-01", "1.5")

    def test_valid_beds2(self, manager):
        with pytest.raises(ValueError, match="Number of beds must be a valid integer."):
            manager.booking(1, "user1", "2026-03-01", -1)

    def test_valid_beds3(self, manager):
        with pytest.raises(ValueError, match="Number of beds must be a valid integer."):
            manager.booking(1, "user1", "2026-03-01", 0)

    def test_valid_beds_string(self, manager):
        with pytest.raises(ValueError, match="Number of beds must be a valid integer."):
            manager.booking(1, "user1", "2026-03-01", "number")

    def test_valid_beds4(self, manager):
        with pytest.raises(ValueError, match="Number of beds must be a valid integer."):
            manager.booking(1, "user1", "2026-03-01", 1.5)

    def test_valid_beds5(self, manager):
        with pytest.raises(ValueError, match="Number of beds must be a valid integer."):
            manager.booking(1, "user1", "2026-03-01", -1.5)

    def test_valid_beds6(self, manager):
        with pytest.raises(ValueError, match="Number of beds must be a valid integer."):
            manager.booking(1, "user1", "2026-03-01", "!@#$")

    def test_booking_none_date(self, manager):
        with pytest.raises(
                ValueError, match="Date must be a valid string in 'YYYY-MM-DD' format."
        ):
            manager.booking(1, "user1", None, 1)

    def test_booking_empty_date(self, manager):
        with pytest.raises(
                ValueError, match="Date must be a valid string in 'YYYY-MM-DD' format."
        ):
            manager.booking(1, "user1", "", 1)

    def test_booking_none_user(self, manager):
        with pytest.raises(ValueError, match="User name must be a valid string."):
            manager.booking(1, None, "2026-03-01", 1)

    def test_booking_empty_user(self, manager):
        with pytest.raises(ValueError, match="User name must be a valid string."):
            manager.booking(1, "", "2026-03-01", 1)


class TestEdgeCases:
    """
    Test suite for edge cases in reservation management.

    These tests cover scenarios like cancelling non-existent bookings,
    booking conflicts, and other boundary conditions.
    """

    def test_cancel_nonexistent_booking(self, manager):
        assert manager.cancelBooking(999) == False

    def test_cancel_booking_verify_removal(self, manager):
        manager.booking(1, "user1", "2026-03-01", 1)
        initial_count = len(manager.reservations)
        manager.cancelBooking(1)
        assert len(manager.reservations) == initial_count - 1

    def test_booking_different_users_same_date(self, manager):
        manager.booking(1, "user1", "2026-03-01", 1)
        manager.booking(2, "user2", "2026-03-01", 1)
        assert len(manager.reservations) == 2
