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

    def cover(self, other):         # najmniejszy okrąg pokrywający oba
        distance_centers = math.sqrt((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2)

        if distance_centers + min(self.radius, other.radius) <= max(self.radius, other.radius):
            if self.radius < other.radius:
                return other
            else:
                return self 
        
        cover_radius = max(self.radius, other.radius) + distance_centers / 2
        
        cover_x = (self.pt.x + other.pt.x) / 2
        cover_y = (self.pt.y + other.pt.y) / 2

        return Circle(cover_x, cover_y, cover_radius)
    
    @classmethod
    def from_points(cls, points):
        if len(points) != 3:
            raise ValueError("Należy podać dokładnie trzy punkty!")
        
        if not all(isinstance(p, Point) for p in points):
            raise ValueError("Wszyskie elementy muszą być instancji Point!")
        
        x1, y1 = points[0].x, points[0].y
        x2, y2 = points[1].x, points[1].y
        x3, y3 = points[2].x, points[2].y

        ma = (y2 - y1) / (x2 -x1) if x2 - x1 != 0 else float('inf')
        mb = (y3 - y2) / (x3 - x2) if x3 - x2 != 0 else float('inf')
        if ma == mb:
            raise ValueError("Podane punkty są współliniowe!")
        
        center_x = (ma * mb * (y1 - y3) + mb * (x1 + x2) - ma * (x2 + x3)) / (2 * (mb - ma))
        center_y = ((-1 / ma) * (center_x - (x1 + x2) / 2) + (y1 + y2) / 2)
        radius = math.sqrt((x1 - center_x) ** 2 + (y1 - center_y) ** 2)

        return cls(center_x, center_y, radius)
    
    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def width(self):
        return 2 * self.radius

    @property
    def height(self):
        return 2 * self.radius

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)