#!/usr/bin/env python3

import sys
from addop import AddOp
from biopexpr import BiOpExpr
from intexpr import IntExpr
from multiop import MultiOp


OPERATOR_MAP = {
    "add": AddOp(),
    "multiply": MultiOp(),
}


def main():
    """ Expects an binary operation expression string as the only argument and
        prints the evaluation result
        eg.
          ./calc.py "(multiply (add 1 2) 3)"
          => 9
    """
    expr_str = sys.argv[1]
    expr = parse(expr_str)
    result = expr.evaluate()
    print(result)
    return


def parse(expr_str):
    # Separate parentheses with spaces for split delimiters
    expr_str = expr_str.replace(')', ' ) ')
    expr_str = expr_str.replace('(', ' ( ')
    words = expr_str.split()
    stack = []
    for i in range(len(words)):
        if words[i] == '(':
            # Next word is an operator so push that as a new operator
            i += 1
            stack.append(OPERATOR_MAP.get(words[i]))
        elif words[i] == ')':
            # Last word for current expression
            # so pop previous 2 expressions and operator
            # then push new Binary Operator Expression
            ex2 = stack.pop()
            ex1 = stack.pop()
            op = stack.pop()
            new_expr = BiOpExpr(op, ex1, ex2)
            stack.append(new_expr)
        elif words[i].isnumeric():
            number = IntExpr(words[i])
            stack.append(number)
    return stack.pop()


if __name__ == '__main__':
    main()
