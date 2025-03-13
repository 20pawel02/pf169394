class Polynomial:
    def __init__(self, coefficients):
        self.coeff = list(coefficients)
        self._remove_leading_zeros()
        if not self.coeff:
            self.coeff = [0]

    def _remove_leading_zeros(self):
        while len(self.coeff) > 1 and self.coeff[0] == 0:
            self.coeff.pop(0)

    def degree(self):
        return len(self.coeff) -1

    def evaluate(self, x):
        wyn = 0
        for coefficient in self.coeff:
            wyn = wyn * x + coefficient
        return wyn
        

    def __str__(self):
        if all(coeff == 0 for coeff in self.coeff):
            return "0"
        
        tab = []
        for i, coeff in enumerate(self.coeff):
            silnia = len(self.coeff) - i - 1
            if coeff == 0:
                continue
            if silnia == 0:
                tab.append(f"{coeff}")
            elif silnia == 1:
                if coeff == 1:
                    tab.append("x")
                elif coeff == -1:
                    tab.append("-x")
                else:
                    tab.append(f"{coeff}x")
            else:
                if coeff == 1:
                    tab.append(f"x^{silnia}")
                elif coeff == -1:
                    tab.append(f"-x^{silnia}")
                else:
                    tab.append(f"{coeff}x^{silnia}")
        return " + ".join(tab).replace("+ -", "- ")
            

    def __repr__(self):
        return f"Polynomial({self.coeff})"

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coeff == other.coeff
        elif isinstance(other, (int, float)):
            return self.degree() == 0 and self.coeff[0] == other
        return False

    def __add__(self, other):
        if isinstance(other, Polynomial):
            max_length = max(len(self.coeff), len(other.coeff))
            self_coeff = [0] * (max_length - len(self.coeff)) + self.coeff
            other_coeff = [0] * (max_length - len(other.coeff)) + other.coeff
            
            new_coeff = [a + b for a, b in zip(self_coeff, other_coeff)]
            return Polynomial(new_coeff)
        elif isinstance(other, (int, float)):
            new_coeff = self.coeff[:]
            new_coeff[-1] += other
            return Polynomial(new_coeff)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            max_length = max(len(self.coeff), len(other.coeff))
            self_coeff = [0] * (max_length - len(self.coeff)) + self.coeff
            other_coeff = [0] * (max_length - len(other.coeff)) + other.coeff
            
            new_coeff = [a - b for a, b in zip(self_coeff, other_coeff)]
            return Polynomial(new_coeff)
        elif isinstance(other, (int, float)):
            new_coeff = self.coeff[:]
            new_coeff[-1] -= other
            return Polynomial(new_coeff)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            nowy_coeff = [-c for c in self.coeff]
            nowy_coeff[-1] += other
            return Polynomial(nowy_coeff)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            new_coeff = [0] * (len(self.coeff) + len(other.coeff) - 1)
            for self_i, self_c in enumerate(self.coeff):
                for other_i, other_c in enumerate(other.coeff):
                    new_coeff[self_i + other_i] += self_c * other_c
            return Polynomial(new_coeff)
        elif isinstance(other, (int, float)):
            new_coeff = [c * other for c in self.coeff]
            return Polynomial(new_coeff)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)