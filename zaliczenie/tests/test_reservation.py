import pytest
from src.reservation import ReservationManagement, Reservation

@pytest.fixture
def manager():
    return ReservationManagement()

def test_booking_room_with_1_bed(manager):
        manager.booking(1,"user1", "2026-03-01", 1)
        assert manager.reservations[0].beds == 1

def test_cancel_booking(manager):
    manager.booking(1,"user1", "2026-03-01", 1)
    manager.booking(2,"user1", "2026-03-02", 1)
    manager.cancelBooking(1)
    assert manager.userReservation(2)

def test_multiple_bookings(manager):
    manager.booking(1,"user1", "2026-03-01", 1)
    manager.booking(2,"user1", "2026-03-02", 2)
    manager.booking(3,"user1", "2026-03-03", 3)
    user_reservations = manager.userReservations()


def test_userReservation(manager):
    manager.booking(1,"user1", "2026-03-01", 1)
    assert manager.userReservation(1)
