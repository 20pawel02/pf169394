import unittest

class ShippingCart():
    def __init__(self):
        self.przedmioty = {}

    def add_item(self, przedmiot, cena):
        if przedmiot in self.przedmioty:
            self.przedmioty[przedmiot] += cena

    def remove_item(self, przedmiot):
        if przedmiot in self.przedmioty:
            del self.przedmioty[przedmiot]

    def get_total(self):
        return sum(self.przedmioty.values())
    
    def clear(self):
        self.przedmioty.clear()