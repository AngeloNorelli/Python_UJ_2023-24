import unittest
from polys import *

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
        with self.assertRaises(ValueError):
            add_poly([1, 2], [3, 'a', 5])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])

    def test_is_zero(self):
        self.assertTrue(is_zero([0]))
        self.assertTrue(is_zero([0, 0, 0]))
        self.assertFalse(is_zero([1, 0, 0]))

    def test_eq_poly(self):
        self.assertTrue(eq_poly(self.p1, [0, 1]))
        self.assertFalse(eq_poly(self.p1, self.p2))

    def test_eval_poly(self):
        self.assertEqual(eval_poly([2, 3, 1], 2), 12)

    def test_combine_poly(self):
        self.assertEqual(combine_poly([1, -1], [0, 1]), [1, -1])

    def test_pow_poly(self):
        self.assertEqual(pow_poly([1, 2], 2), [1, 4, 4])

    def test_diff_poly(self):
        self.assertEqual(diff_poly([3, 2, 1]), [2, 2])

    def tearDown(self):
        pass

if __name__ == '_main_':
    unittest.main()