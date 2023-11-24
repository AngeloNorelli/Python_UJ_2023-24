import unittest
from circles import *

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle1 = Circle(1, 2, 5)
        self.circle2 = Circle(1, 2, 7)
        self.circle3 = Circle(1, 2, 5.0)

    def test_init(self):
        with self.assertRaises(ValueError):
            alpha = Circle('a', 2, 0)
        with self.assertRaises(ValueError):
            beta = Circle(1, 1, -2)

    def test_repr(self):
        self.assertEqual(repr(self.circle1), "Circle(1, 2, 5)")
        self.assertEqual(repr(self.circle2), "Circle(1, 2, 7)")

    def test_eq(self):
        self.assertEqual(self.circle3, self.circle1)
        self.assertEqual(self.circle2, Circle(1.0, 2.0, 7.0))

    def test_ne(self):
        self.assertNotEqual(self.circle2, self.circle1)
        self.assertNotEqual(self.circle3, self.circle2)

    def test_area(self):
        self.assertAlmostEqual(self.circle1.area(), 78.539, places=2)
        self.assertAlmostEqual(self.circle2.area(), 153.938, places=2)
        self.assertAlmostEqual(self.circle3.area(), 78.539, places=2)

    def test_move(self):
        self.circle1.move(2.5, 1.75)
        self.assertEqual(repr(self.circle1), "Circle(3.5, 3.75, 5)")
        self.circle2.move(3.33, 2)
        self.assertEqual(repr(self.circle2), "Circle(4.33, 4, 7)")
        self.circle3.move(10, 200.1)
        self.assertEqual(repr(self.circle3), "Circle(11, 202.1, 5.0)")
        with self.assertRaises(ValueError):
            self.circle1.move('a', 2)
        with self.assertRaises(ValueError):
            self.circle2.move(3, '2')

    def test_cover(self):
        covering_circle1 = self.circle2.cover(self.circle3)
        self.assertEqual(repr(covering_circle1), "Circle(1, 2, 7)")
        covering_circle2 = self.circle1.cover(Circle(9, 10, 1))
        self.assertEqual(repr(covering_circle2), "Circle(5.0, 6.0, 16.31370849898476)")

if __name__ == '__main__':
    unittest.main()