import re


class Reservation:
    """
    Represents a single room reservation with its details.

    Attributes:
        id (int): The user's unique identifier.
        reservation_number (int): Unique identifier for the reservation.
        beds (int): Number of beds booked.
        user (str): Name of the user making the reservation.
        date (str): Date of the reservation in 'YYYY-MM-DD' format.
    """

    def __init__(
        self, id: int, reservation_number: int, beds: int, user: str, date: str
    ):
        self.id = id
        self.reservation_number = reservation_number
        self.beds = beds
        self.user = user
        self.date = date


class ReservationManagement:
    """
    Manages room reservations, providing methods for booking and cancelling reservations.

    Attributes:
        reservations (list): A list of Reservation objects tracking all current bookings.
    """

    def __init__(self):
        self.reservations = []

    def booking(self, id: int, user: str, date: str, beds: int):
        """
        Book a room for a user on a specific date.

        Args:
            id (int): User's unique identifier.
            user (str): Name of the user making the reservation.
            date (str): Date of the reservation in 'YYYY-MM-DD' format.
            beds (int): Number of beds to book.

        Raises:
            ValueError: If input validation fails or reservation conflicts exist.
        """
        # input validation
        if not id or not isinstance(id, int) or id <= 0:
            raise ValueError("User ID must be a valid integer.")
        if not user or not isinstance(user, str):
            raise ValueError("User name must be a valid string.")
        if not re.match(r"^[a-zA-Z0-9]+$", user):
            raise ValueError("User name must contain only letters and numbers.")
        if not date or not isinstance(date, str):
            raise ValueError("Date must be a valid string in 'YYYY-MM-DD' format.")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            raise ValueError("Date must be a valid string in 'YYYY-MM-DD' format.")
        if not beds or not isinstance(beds, int) or beds < 0:
            raise ValueError("Number of beds must be a valid integer.")

        # checking conflicting reservations
        for existing_reservation in self.reservations:
            if (
                existing_reservation.id == id
                and existing_reservation.user == user
                and existing_reservation.date == date
            ):
                raise ValueError("User already booked room(s) on this date.")

        # creating new reservation id
        newID = len(self.reservations) + 1
        newReservation = Reservation(id, newID, beds, user, date)
        self.reservations.append(newReservation)

    def cancelBooking(self, id):
        """
        Cancel a reservation for a given user ID.

        Args:
            id (int): User's unique identifier to cancel reservation for.

        Returns:
            bool: True if reservation was cancelled, False otherwise.
        """
        for existing_reservation in self.reservations:
            if existing_reservation.id == id:
                self.reservations.remove(existing_reservation)
                return True
        return False

    def userReservation(self, id: int):
        """
        Retrieve a list of reservations for a given user ID.

        Args:
            id (int): User's unique identifier.

        Returns:
            list: A list of Reservation objects for the given user ID.

        Raises:
            ValueError: If user ID is not a valid integer.
        """
        # check if id is valid
        if not isinstance(id, int):
            raise ValueError("User ID must be a valid integer.")

        # creating user reservations list
        user_reservations = []
        for reservation in self.reservations:
            if reservation.id == id:
                user_reservations.append(reservation)
        return user_reservations