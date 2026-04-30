import unittest
from src.MathEvalLib_NDev08 import MathEvalLib

class TestMultiplicationDivision(unittest.TestCase):
    def setUp(self):
        self.math_eval = MathEvalLib()

    def test_multiplication(self):
        self.assertEqual(self.math_eval.evaluate("2 * 3"), 6)
        self.assertEqual(self.math_eval.evaluate("10 * 5 * 2"), 100)
        self.assertEqual(self.math_eval.evaluate("1 * 2 * 3 * 4 * 5"), 120)

    def test_division(self):
        self.assertEqual(self.math_eval.evaluate("6 / 2"), 3)
        self.assertEqual(self.math_eval.evaluate("100 / 5 / 2"), 10)
        self.assertEqual(self.math_eval.evaluate("120 / 1 / 2 / 3 / 4 / 5"), 1)

    def test_mixed_multiplication_and_division(self):
        self.assertEqual(self.math_eval.evaluate("10 * 5 / 2"), 25)
        self.assertEqual(self.math_eval.evaluate("100 / 5 * 2"), 40)
        self.assertEqual(self.math_eval.evaluate("120 / 1 * 2 / 3 * 4 / 5"), 64)

if __name__ == "__main__":
    unittest.main()
