class User:
    def __init__(self, id: int, email: str, password: str):
        self.id = id
        self.email = email
        self.password = password
        self.reservations = []


class UserManagement:
    def __init__(self) -> None:
        self.users = {}

    def addUser(self, email: str, password: str):
        # chceck if user already exists
        for user in self.users.values():
            if user.email == email:
                raise ValueError("User already exists.")

        # input validation
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a valid string.")
        if len(password) < 8:
            raise ValueError("Password must be longer than 8 characters.")

        # creating user
        userID = len(self.users) + 1
        self.users[userID] = User(userID, email, password)
        return userID

    def updateUser(self, id: int, email: str, password: str):
        # check if user exists
        if id not in self.users:
            raise ValueError("User not exists.")

        # input validation
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a valid string.")
        if len(password) < 8:
            raise ValueError("Password must be longer than 8 characters.")

        for user in self.users.values():
            if user.id != id and user.email == email:
                raise ValueError("Email already exists.")

        # updating data
        self.users[id].email = email
        self.users[id].password = password

    def deleteUser(self, id: int):
        # chceck if user exist in users
        if id not in self.users:
            raise ValueError("User is not existing.")

        # check if user have existing reservations
        if self.users[id].reservations:
            raise ValueError("User have existing reservations.")

        del self.users[id]

    def getUser(self, id: int):
        return self.users.get(id, None)
