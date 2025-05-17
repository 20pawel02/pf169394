import re


class Reservation:
    def __init__(
            self, id: int, reservation_number: int, beds: int, user: str, date: str
    ):
        self.id = id
        self.reservation_number = reservation_number
        self.beds = beds
        self.user = user
        self.date = date


class ReservationManagement:
    def __init__(self):
        self.reservations = []

    def booking(self, id: int, user: str, date: str, beds: int):
        # input validation
        if id is None or not isinstance(id, int) or id <= 0:
            raise ValueError("User ID must be a valid integer.")
        if not isinstance(user, str) or not user:
            raise ValueError("User name must be a valid string.")
        if not re.match(r"^[a-zA-Z0-9]+$", user):
            raise ValueError("User name must contain only letters and numbers.")
        if not isinstance(date, str) or not date:
            raise ValueError("Date must be a valid string in 'YYYY-MM-DD' format.")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            raise ValueError("Date must be a valid string in 'YYYY-MM-DD' format.")
        if beds is None or not isinstance(beds, int) or beds <= 0:
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
        reservations_to_remove = []
        for reservation in self.reservations:
            if reservation.id == id:
                reservations_to_remove.append(reservation)

        if not reservations_to_remove:
            return False

        for reservation in reservations_to_remove:
            self.reservations.remove(reservation)
        return True

    def userReservation(self, id: int):
        if id is None or not isinstance(id, int):
            raise ValueError("User ID must be a valid integer.")

        # creating user reservations list
        user_reservations = []
        for reservation in self.reservations:
            if reservation.id == id:
                user_reservations.append(reservation)
        return user_reservations
