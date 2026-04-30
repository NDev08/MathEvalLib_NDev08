import unittest
from src.MathEvalLib_NDev08 import MathEvalLib

class TestAdditionSubtraction(unittest.TestCase):
    def setUp(self):
        self.math_eval = MathEvalLib()

    def test_addition(self):
        self.assertEqual(self.math_eval.evaluate("2 + 3"), 5)
        self.assertEqual(self.math_eval.evaluate("10 + 5 + 2"), 17)
        self.assertEqual(self.math_eval.evaluate("1 + 2 + 3 + 4 + 5"), 15)

    def test_subtraction(self):
        self.assertEqual(self.math_eval.evaluate("5 - 2"), 3)
        self.assertEqual(self.math_eval.evaluate("10 - 5 - 2"), 3)
        self.assertEqual(self.math_eval.evaluate("20 - 5 - 3 - 2"), 10)

    def test_mixed_addition_and_subtraction(self):
        self.assertEqual(self.math_eval.evaluate("10 + 5 - 3"), 12)
        self.assertEqual(self.math_eval.evaluate("20 - 5 + 3 - 2"), 16)
        self.assertEqual(self.math_eval.evaluate("1 + 2 - 3 + 4 - 5"), -1)

if __name__ == "__main__":
    unittest.main()
