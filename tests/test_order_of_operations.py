import unittest
from src.MathEvalLib_NDev08 import MathEvalLib

class TestOrderOfOperations(unittest.TestCase):
    def setUp(self):
        self.math_eval = MathEvalLib()

    def test_order_of_operations(self):
        self.assertEqual(self.math_eval.evaluate("(2 + 3) * 4"), 20)
        self.assertEqual(self.math_eval.evaluate("10 - (5 + 2)"), 3)
        self.assertEqual(self.math_eval.evaluate("1 + 2 * 3 - 4"), 3)
        self.assertEqual(self.math_eval.evaluate("10^4 / 2 + 5"), 5005)
        self.assertEqual(self.math_eval.evaluate("(100 / 5)^2 - 2"), 398)
        self.assertEqual(self.math_eval.evaluate("120 / (1 * 2) / 3 * 4 / 5"), 16)