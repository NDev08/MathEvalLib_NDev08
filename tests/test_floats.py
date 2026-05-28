import unittest
from MathEvalLib_NDev08 import MathEvalLib


class TestFloats(unittest.TestCase):
    def setUp(self):
        self.math_eval = MathEvalLib()

    def testFloats(self):
        self.assertEqual(self.math_eval.evaluate("2.5 + 3.1"), 5.6)
        self.assertEqual(self.math_eval.evaluate("5.0 - 2.5"), 2.5)
        self.assertEqual(self.math_eval.evaluate("3.2 * 4.0"), 12.8)
        self.assertEqual(self.math_eval.evaluate("10.0 / 2.0"), 5.0)
        self.assertEqual(self.math_eval.evaluate("2.5 ^ 3"), 15.625)
