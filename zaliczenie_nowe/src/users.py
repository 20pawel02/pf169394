class User:
    """
    Represents a user with their basic information and reservations.

    Attributes:
        id (int): Unique identifier for the user.
        email (str): User's email address.
        password (str): User's password.
        reservations (list): List of user's reservations.
    """
    def __init__(self, id: int, email: str, password: str):
        self.id = id
        self.email = email
        self.password = password
        self.reservations = []


class UserManagement:
    """
    Manages user accounts with methods to add, update, and delete users.

    Attributes:
        users (dict): A dictionary of users, keyed by their unique ID.
        next_id (int): Incremental ID for creating new users.
    """
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def addUser(self, email: str, password: str):
        """
        Add a new user to the system.

        Args:
            email (str): User's email address.
            password (str): User's password.

        Returns:
            int: The unique ID of the newly created user.

        Raises:
            ValueError: If email already exists or input validation fails.
        """
        # chceck if user already exists
        for user in self.users.values():
            if user.email == email:
                raise ValueError("User already exists.")

        # input validation
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a valid string.")
        if not password or not isinstance(password, str) or len(password) < 8:
            raise ValueError("Password must be longer than 8 characters.")

        # creating user
        user_id = self.next_id
        self.users[user_id] = User(user_id, email, password)
        self.next_id += 1
        return user_id

    def updateUser(self, id: int, email: str, password: str):
        """
        Update an existing user's email and password.

        Args:
            id (int): User's unique identifier.
            email (str): New email address.
            password (str): New password.

        Raises:
            ValueError: If user doesn't exist, email is invalid, or email already exists.
        """
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
        """
        Delete a user from the system.

        Args:
            id (int): User's unique identifier.

        Raises:
            ValueError: If user does not exist or has existing reservations.
        """
        # chceck if user exist in users
        if id not in self.users:
            raise ValueError("User is not existing.")

        # check if user have existing reservations
        if self.users[id].reservations:
            raise ValueError("User have existing reservations.")

        del self.users[id]

    def getUser(self, id: int):
        """
        Retrieve a user by their unique ID.

        Args:
            id (int): User's unique identifier.

        Returns:
            User: The user with the matching ID, or None if not found.
        """
        return self.users.get(id, None)
