import math

class Frac:
    """Klasa reprezentująca ułamek."""

    def _lcm(self, a, b):
        return abs(a *b) // math.gcd(a, b) if a and b else 0

    def _reduce(self):
        gcd = math.gcd(self.x, self.y)
        return Frac(self.x // gcd, self.y // gcd)

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):              # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        return f"{self.x}/{self.y}"

    def __repr__(self):             # zwraca "Frac(x, y)"
        return f"Frac({self.x}, {self.y})"

    def __eq__(self, other):        # Py2.7 i Py3
        return self.x * other.y == other.x * self.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.x * other.y < other.x * self.y

    def __le__(self, other):
        return self.x * other.y <= other.x * self.y

    def __gt__(self, other):
        return self.x * other.y > other.x * self.y

    def __ge__(self, other):
        return self.x * other.y >= other.x * self.y

    def __cmp__(self, other):       # cmp(frac1, frac2)    # Py2
        if self < other:
            return -1
        if self > other:
            return 1
        return 0

    def __add__(self, other):       # frac1 + frac2
        return Frac(self.x * other.y + other.x * self.y, self.y * other.y)._reduce()

    def __sub__(self, other):       # frac1 - frac2
        return Frac(self.x * other.y - other.x * self.y, self.y * other.y)._reduce()

    def __mul__(self, other):       # frac1 * frac2
        return Frac(self.x * other.x, self.y * other.y)._reduce()

    def __div__(self, other):       # frac1 / frac2, Py2
        return Frac(self.x * other.y, self.y * other.x)._reduce()

    def __truediv__(self, other):   # frac1 / frac2, Py3
        return (self.x * other.y) / (self.y * other.x)

    def __floordiv__(self, other):  # frac1 // frac2, opcjonalnie
        return self.x * other.y // (self.y * other.x)

    def __mod__(self, other):       # frac1 % frac2, opcjonalnie
        numerator = self.x * other.y
        denominator = self.y * other.x
        return Frac(numerator % denominator, self.y * other.y)._reduce()

    # operatory jednoargumentowe
    def __pos__(self):      # +frac = (+1)*frac
        return self

    def __neg__(self):      # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):   # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):    # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])
