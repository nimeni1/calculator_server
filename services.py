import cexprtk


class Parser:
    def __init__(self):
        """Parser constructor."""
        self.expression = ""

    def set_expression(self, expression):
        """Set parser expression to be checked and evaluated."""
        self.expression = expression

    def check_expression(self):
        """Check parser expression to be evaluated."""
        if cexprtk.check_expression(self.expression) is not None:
            return False
        return True

    def evaluate_expression(self):
        """Ëvaluate parser expression."""
        result = cexprtk.evaluate_expression(self.expression, {})
        return result
