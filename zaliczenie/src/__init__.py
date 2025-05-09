class Reservation:
    def __init__(self, id: int, reservation_number: int, rooms: int, user: str, date: str):
        self.id = id
        self.reservation_number = reservation_number
        self.rooms = rooms
        self.user = user
        self.date = date

class User:
    def __init__(self, id: int, email: str, password: str):
        self.id = id
        self.email = email
        self.password = password