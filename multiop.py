from op import Op


class MultiOp(Op):
    def execute(self, left_expr, right_expr):
        return left_expr.evaluate() * right_expr.evaluate()
