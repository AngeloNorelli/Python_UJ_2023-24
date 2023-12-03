from circles import *
from points import *
import pytest

def test_circle_creation():
    circle = Circle(0, 0, 5)
    assert circle.pt == Point(0, 0)
    assert circle.radius == 5

def test_circle_area():
    circle = Circle(0, 0, 5)
    assert circle.area() == pytest.approx(78.54, rel=1e-2)

def test_circle_move():
    circle = Circle(0, 0, 5)
    circle.move(3, 4)
    assert circle.pt == Point(3, 4)

def test_circle_cover():
    circle1 = Circle(0, 0, 5)
    circle2 = Circle(0, 0, 3)
    circle3 = Circle(10, 10, 13)

    assert circle1.cover(circle2) == circle1
    assert circle1.cover(circle3) == circle3
    assert circle2.cover(circle3) == circle3

def test_circle_from_points():
    point1 = Point(0, 0)
    point2 = Point(3, 0)
    point3 = Point(0, 4)
    circle = Circle.from_points((point1, point2, point3))

    assert circle.pt == Point(1.5, 2)
    assert circle.radius == pytest.approx(2.5, rel=1e-2)