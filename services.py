import cexprtk


class Parser:
    def __init__(self):
        self.expression = ""

    def set_expression(self, expression):
        self.expression = expression

    def evaluate_expression(self):
        result = cexprtk.evaluate_expression(self.expression, {})
        return result
