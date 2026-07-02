class MathEvalError(Exception):
    """Base exception for the library."""

    pass


class ExpressionSyntaxError(ValueError, MathEvalError):
    """Invalid mathematical expression."""

    pass


class EvaluationError(MathEvalError):
    """Expression could not be evaluated."""

    pass


class DivisionByZeroError(EvaluationError):
    """Attempted to divide by zero."""

    pass
