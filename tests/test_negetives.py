import unittest
from MathEvalLib_NDev08 import MathEvalLib


class TestNegatives(unittest.TestCase):
    def setUp(self):
        self.math_eval = MathEvalLib()

    def test_negatives(self):
        self.assertEqual(self.math_eval.evaluate("-10+5"), -5)
        self.assertEqual(self.math_eval.evaluate("10+-5"), 5)
        self.assertEqual(self.math_eval.evaluate("-10+-5"), -15)
        self.assertEqual(self.math_eval.evaluate("-10+5+5+-2"), -2)
