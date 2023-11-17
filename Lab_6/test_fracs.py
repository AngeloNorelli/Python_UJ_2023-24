import unittest
import math
from fracs import *

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.frac1 = Frac(3, 4)
        self.frac2 = Frac(2, 3)
        self.frac3 = Frac(6, 8)
        self.frac4 = Frac(1, 2)

    def test_str(self):
        self.assertEqual(str(self.frac1), "3/4")
        self.assertEqual(str(self.frac4), "1/2")
        self.assertEqual(str(Frac(5, 1)), "5")

    def test_repr(self):
        self.assertEqual(repr(self.frac1), "Frac(3, 4)")
        self.assertEqual(repr(self.frac4), "Frac(1, 2)")

    def test_eq(self):
        self.assertEqual(self.frac1, self.frac3)
        self.assertNotEqual(self.frac1, self.frac2)

    def test_ne(self):
        self.assertNotEqual(self.frac1, self.frac2)
        self.assertNotEqual(self.frac1, self.frac4)

    def test_lt(self):
        self.assertTrue(self.frac4 < self.frac1)
        self.assertFalse(self.frac1 < self.frac4)

    def test_le(self):
        self.assertTrue(self.frac1 <= self.frac3)
        self.assertTrue(self.frac4 <= self.frac1)
        self.assertFalse(self.frac1 <= self.frac4)

    def test_gt(self):
        self.assertTrue(self.frac1 > self.frac4)
        self.assertFalse(self.frac4 > self.frac1)

    def test_ge(self):
        self.assertTrue(self.frac3 >= self.frac1)
        self.assertTrue(self.frac1 >= self.frac4)
        self.assertFalse(self.frac4 >= self.frac2)

    def test_add(self):
        self.assertEqual(self.frac1 + self.frac2, Frac(17, 12))

    def test_sub(self):
        self.assertEqual(self.frac1 - self.frac2, Frac(1, 12))

    def test_mul(self):
        self.assertEqual(self.frac1 * self.frac2, Frac(1, 2))

    def test_truediv(self):
        self.assertEqual(self.frac1 / self.frac2, 9 / 8)

    def test_floordiv(self):
        self.assertEqual(self.frac1 // self.frac2, 1)

    def test_mod(self):
        self.assertEqual(self.frac1 % self.frac2, Frac(1, 12))

    def test_pos(self):
        self.assertEqual(+self.frac1, self.frac1)

    def test_neg(self):
        self.assertEqual(-self.frac1, Frac(-3, 4))

    def test_invert(self):
        self.assertEqual(~self.frac1, Frac(4, 3))

    def test_float(self):
        self.assertAlmostEqual(float(self.frac1), 0.75)
        self.assertAlmostEqual(float(self.frac4), 0.5)

    def test_hash(self):
        self.assertEqual(hash(self.frac1), hash(Frac(6, 8)))

    if __name__ == '__main__':
        unittest.main()

