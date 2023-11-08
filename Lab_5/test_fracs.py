import unittest
from fracs import *

class TestFractions(unittest.TestCase):

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([3, 4], [1, 4]), [1, 1])
        with self.assertRaises(ValueError):
            add_frac([1, 2], 3)
        with self.assertRaises(ValueError):
            add_frac([1, 2], [1, 0])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([3, 4], [1, 4]), [1, 2])
        with self.assertRaises(ValueError):
            sub_frac([1, 2], "abc")

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, -3]), [-1, 6])
        self.assertEqual(mul_frac([3, 4], [1, 4]), [3, 16])
        with self.assertRaises(ValueError):
            mul_frac([1, 2], [1, 0])
        with self.assertRaises(ValueError):
            mul_frac([1, 2], [1, "2"])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([3, 4], [1, 4]), [3, 1])
        with self.assertRaises(ValueError):
            div_frac([1, 2], 3)
        with self.assertRaises(ValueError):
            div_frac([1, 2], [1, 0])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        with self.assertRaises(ValueError):
            is_positive([1.5, 2])

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 5]))
        self.assertFalse(is_zero([1, 2]))
        with self.assertRaises(ValueError):
            is_zero([0, 0])

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([2, 3], [2, 3]), 0)
        with self.assertRaises(ValueError):
            cmp_frac([1, 2], "abc")

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5)
        self.assertAlmostEqual(frac2float([3, 4]), 0.75)
        with self.assertRaises(ValueError):
            frac2float([1, 0])

if __name__ == '_main_':
    unittest.main()