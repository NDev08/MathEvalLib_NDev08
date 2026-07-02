import unittest
from MathEvalLib_NDev08 import MathEvalLib


class TestErrorChecking(unittest.TestCase):
    def setUp(self):
        self.math_eval = MathEvalLib()

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            self.math_eval.evaluate("2 + 3a")

    def test_unmatched_parentheses(self):
        with self.assertRaises(ValueError):
            self.math_eval.evaluate("(2 + 3")
        with self.assertRaises(ValueError):
            self.math_eval.evaluate("2 + 3)")

    def test_operator_at_start_or_end(self):
        with self.assertRaises(ValueError):
            self.math_eval.evaluate("+2 + 3")
        with self.assertRaises(ValueError):
            self.math_eval.evaluate("2 + 3-")

    def test_consecutive_operators(self):
        with self.assertRaises(ValueError):
            self.math_eval.evaluate("2 ++ 3")
        with self.assertRaises(ValueError):
            self.math_eval.evaluate("2 +* 3")
        with self.assertRaises(ValueError):
            self.math_eval.evaluate("2 ^/ 3")
        with self.assertRaises(ValueError):
            self.math_eval.evaluate("2 --- 3")
