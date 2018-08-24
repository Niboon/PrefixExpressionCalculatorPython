from expr import Expr


class IntExpr(Expr):
    """
    Fields: _value (str)
    """

    def __init__(self, value):
        self._value = value

    def evaluate(self):
        return int(self._value)
