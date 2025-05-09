class Reservation:
    def __init__(self, id: int, reservation_number: int, rooms: int, user: str, date: str):
        self.id = id
        self.reservation_number = reservation_number
        self.rooms = rooms
        self.user = user
        self.date = date

class Management:
    def __init__(self):
        self.reservations = []

    def booking(self, id: int, name: str, date: str):
        # input validation
        if not id or not isinstance(id, int):
            raise ValueError("User ID must be a valid integer.")
        if not name or not isinstance(name, str):
            raise ValueError("User name must be a valid string.")
        if not date or not isinstance(date, str):
            raise ValueError("Date must be a valid string in 'YYYY-MM-DD' format.")

        # checking conflicting reservations
        for existing_reservation in self.reservations:
            if existing_reservation.id == id and existing_reservation.name == name and existing_reservation.date == date:
                raise ValueError(f"User {id} {name} already booked room(s) on {date}.")

        # creating new reservation id
        newID = len(self.reservations) + 1
        newReservation = Reservation(id, newID, name, , date, )
        self.reservations.append(newReservation)

    def cancel_booking(self, id):
        for existing_reservation in self.reservations:
            if existing_reservation.id == id:
                self.reservations.remove(existing_reservation)
                return True
        return False

    def user_reservation(self, id: int):
        users = []
        for existing_reservation in self.reservations:
            if existing_reservation.id == id:
                users.append(existing_reservation)
            return users