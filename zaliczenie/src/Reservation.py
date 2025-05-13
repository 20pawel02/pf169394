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
        if not id or not isinstance(id, int):
            raise ValueError("User ID must be a valid integer.")
        if not user or not isinstance(user, str):
            raise ValueError("User name must be a valid string.")
        if not date or not isinstance(date, str):
            raise ValueError("Date must be a valid string in 'YYYY-MM-DD' format.")

        # checking conflicting reservations
        for existing_reservation in self.reservations:
            if (
                    existing_reservation.id == id
                    and existing_reservation.user == user
                    and existing_reservation.date == date
            ):
                raise ValueError(f"User {id} {user} already booked room(s) on {date}.")

        # creating new reservation id
        newID = len(self.reservations) + 1
        newReservation = Reservation(id, newID, beds, user, date)
        self.reservations.append(newReservation)

    def cancelBooking(self, id):
        for existing_reservation in self.reservations:
            if existing_reservation.id == id:
                self.reservations.remove(existing_reservation)
                return True
        return False

    def userReservation(self, id: int):
        # check if id is valid
        if not isinstance(id, int):
            raise ValueError("User ID must be a valid integer.")

        # creating user reservations list
        user_reservations = []
        for reservation in self.reservations:
            if reservation.id == id:
                user_reservations.append(reservation)
        return user_reservations
