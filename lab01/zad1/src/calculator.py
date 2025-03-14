class Kalkulator:
    def __init__(self):
        pass

    def dodawanie(self, a, b):
        return a + b

    def odejmowanie(self, a, b):
        return a - b

    def mnozenie(self, a, b):
        return a * b

    def dzielenie(self, a, b):
        if b == 0:
            raise ValueError("Nie dziel przez 0!")
        return a / b
   