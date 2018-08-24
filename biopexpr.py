from expr import Expr


class BiOpExpr(Expr):
    """
    Fields: _leftExpr (Expr),
            _rightExpr (Expr),
            _op (Op),
    """

    def __init__(self, op, left_expr, right_expr):
        self._op = op
        self._leftExpr = left_expr
        self._rightExpr = right_expr

    def evaluate(self):
        return self._op.execute(self._leftExpr, self._rightExpr)
