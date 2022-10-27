import cexprtk


class Parser:
    def __init__(self):
        self.expression = ""

    def set_expression(self, expression):
        self.expression = expression

    def check_expression(self):
        if cexprtk.check_expression(self.expression) is not None:
            return False
        return True

    def evaluate_expression(self):
        result = cexprtk.evaluate_expression(self.expression, {})
        return result
