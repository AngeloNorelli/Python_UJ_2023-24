import unittest
from points import *

class TestPoint(unittest.TestCase):

    def test_str_representation(self):
        p = Point(3, 4)
        self.assertEqual(str(p), "(3, 4)")

    def test_repr_representation(self):
        p = Point(1, 2)
        self.assertEqual(repr(p), "Point(1, 2)")

    def test_equality(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(3, 4)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_addition(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1 + p2
        self.assertEqual(result, Point(4, 6))

    def test_subtraction(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p2 - p1
        self.assertEqual(result, Point(2, 2))

    def test_multiplication(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1 * p2
        self.assertEqual(result, 11)

    def test_cross_product(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1.cross(p2)
        self.assertEqual(result, -2)

    def test_length(self):
        p = Point(3, 4)
        result = p.length()
        self.assertAlmostEqual(result, 5.0, places=2)  # Sprawdzamy, czy długość jest bliska 5.0

    if __name__ == '__main__':
        unittest.main()
