from op import Op


class AddOp(Op):
    def execute(self, left_expr, right_expr):
        return left_expr.evaluate() + right_expr.evaluate()
