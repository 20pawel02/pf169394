class User:
    """
    Klasa reprezentująca użytkownika w systemie.

    Attributes:
        id (int): Unikalny identyfikator użytkownika
        email (str): Adres email użytkownika
        password (str): Hasło użytkownika
        reservations (list): Lista rezerwacji użytkownika
    """
    def __init__(self, id: int, email: str, password: str):
        """
        Inicjalizuje nowego użytkownika.

        Args:
            id (int): Identyfikator użytkownika
            email (str): Adres email
            password (str): Hasło (minimum 8 znaków)
        """
        self.id = id
        self.email = email
        self.password = password
        self.reservations = []


class UserManagement:
    """
    Klasa zarządzająca systemem użytkowników.

    Umożliwia dodawanie, aktualizację, usuwanie i pobieranie użytkowników.
    Każdy użytkownik jest identyfikowany przez unikalny identyfikator.

    Attributes:
        users (dict): Słownik przechowujący wszystkich użytkowników
        next_id (int): Następny dostępny identyfikator użytkownika
    """
    def __init__(self):
        """Inicjalizuje nowy system zarządzania użytkownikami."""
        self.users = {}
        self.next_id = 1

    def addUser(self, email: str, password: str):
        """
        Dodaje nowego użytkownika do systemu.

        Args:
            email (str): Adres email użytkownika
            password (str): Hasło użytkownika (minimum 8 znaków)

        Returns:
            int: Identyfikator nowego użytkownika

        Raises:
            ValueError: Gdy email już istnieje lub gdy dane są nieprawidłowe
        """
        # check if user already exists
        for user in self.users.values():
            if user.email == email:
                raise ValueError("User already exists.")

        # input validation
        if not isinstance(email, str) or not email:
            raise ValueError("Email must be a valid string.")
        if not isinstance(password, str) or len(password) < 8:
            raise ValueError("Password must be longer than 8 characters.")

        # creating user
        user_id = self.next_id
        self.users[user_id] = User(user_id, email, password)
        self.next_id += 1
        return user_id

    def updateUser(self, id: int, email: str, password: str):
        """
        Aktualizuje dane istniejącego użytkownika.

        Args:
            id (int): Identyfikator użytkownika
            email (str): Nowy adres email
            password (str): Nowe hasło (minimum 8 znaków)

        Raises:
            ValueError: Gdy użytkownik nie istnieje, email jest już zajęty
                      lub gdy dane są nieprawidłowe
        """
        # check if user exists
        if id not in self.users:
            raise ValueError("User not exists.")

        # input validation
        if not isinstance(email, str) or not email:
            raise ValueError("Email must be a valid string.")
        if not isinstance(password, str) or len(password) < 8:
            raise ValueError("Password must be longer than 8 characters.")

        for user in self.users.values():
            if user.id != id and user.email == email:
                raise ValueError("Email already exists.")

        # updating data
        self.users[id].email = email
        self.users[id].password = password

    def deleteUser(self, id: int):
        """
        Usuwa użytkownika z systemu.

        Args:
            id (int): Identyfikator użytkownika do usunięcia

        Raises:
            ValueError: Gdy użytkownik nie istnieje lub ma aktywne rezerwacje
        """
        # check if user exist in users
        if id not in self.users:
            raise ValueError("User is not existing.")

        # check if user have existing reservations
        if self.users[id].reservations:
            raise ValueError("User have existing reservations.")

        del self.users[id]

    def getUser(self, id: int):
        """
        Pobiera użytkownika o podanym ID.

        Args:
            id (int): Identyfikator użytkownika

        Returns:
            User or None: Obiekt użytkownika lub None jeśli użytkownik nie istnieje
        """
        return self.users.get(id, None)
