from points import Point
import math

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        # Sprawdzenie poprawnosci wspolrzednych x i y nastepuje
        # podczas tworzenia obiektu Point
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):             # "Circle(x, y, radius)"
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):                 # pole powierzchni
        return self.radius ** 2 * math.pi

    def move(self, x, y):           # przesuniecie o (x, y)
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("Wspolrzedne do przesuniecia musza byc liczbami")
        self.pt = Point(self.pt.x + x, self.pt.y + y)

    def covers(self, other):
        distance = math.sqrt((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2)
        return distance + other.radius <= self.radius

    def cover(self, other):         # najmniejszy okrąg pokrywający oba
        if(self.covers(other)):
            return self
        
        if(other.covers(self)):
            return other

        x = (self.pt.x + other.pt.x) / 2
        y = (self.pt.y + other.pt.y) / 2
        distance = math.sqrt((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2)
        
        return Circle(x, y, distance + max(self.radius, other.radius))