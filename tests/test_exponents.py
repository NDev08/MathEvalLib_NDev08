import unittest
from MathEvalLib_NDev08 import MathEvalLib


class TestExponents(unittest.TestCase):
    def setUp(self):
        self.math_eval = MathEvalLib()

    def testExponents(self):
        self.assertEqual(self.math_eval.evaluate("2 ^ 3"), 8)
        self.assertEqual(self.math_eval.evaluate("5 ^ 0"), 1)
        self.assertEqual(self.math_eval.evaluate("3 ^ 4"), 81)
        self.assertEqual(self.math_eval.evaluate("10 ^ 2"), 100)
        self.assertEqual(self.math_eval.evaluate("2^(3^2)"), 512)
