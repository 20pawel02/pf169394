class BankAccount:
    def __init__(self):
        self.saldo = 0.0

    def deposit(self, kwota):
        if kwota <= 0:
            raise ValueError("nie mozesz wplacic wartosci ujemnej")
        self.saldo += kwota

    def withdraw(self, kwota):
        if kwota <= 0:
            raise ValueError("nie mozesz wyplacic wiecej niz masz")
        if kwota > self.saldo:
            self.saldo -= kwota

    def get_balance(self):
        return self.saldo