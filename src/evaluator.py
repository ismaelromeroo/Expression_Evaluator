"""
Utilizing stacks it evaluates the RPN (Reverse Polish Notation)
to ultimately get the final answer to the original string expression
"""

import operator

OPERATORS = {'+': operator.add ,'-':operator.sub,'*':operator.mul,'/':operator.truediv,"^": lambda a,b: a**b}

def eval_rpn(rpn_tokens: list[tuple[str, int | float | str]], trace: bool = False) -> float:
    stack: list[float] = []

    def log(msg: str):
        if trace:
            print(msg)

    for tok_type, tok_value in rpn_tokens:
        match tok_type:
            case "NUM":
                stack.append(tok_value)
                log(f"push {tok_value} -> {stack}")

            case "OP":
                if tok_value == "NEG":
                    if len(stack) < 1:
                        raise ValueError("Not enough operands for NEG")
                    a = stack.pop()
                    stack.append(-a)
                    log(f"NEG {a} -> {-a} ; stack {stack}")
                    continue

                if len(stack) < 2:
                    raise ValueError("Not enough operands")
                
                b = stack.pop()
                a = stack.pop()

                func = OPERATORS.get(tok_value)
                if func is None:
                    raise ValueError(f"Invalid operator: {tok_value!r}")

                try:
                    res = func(a, b)
                except ZeroDivisionError:
                    raise ValueError("Division by zero") from None

                stack.append(res)
                log(f"{a} {tok_value} {b} -> {res} ; stack {stack}")

            case _:
                raise ValueError(f"Bad token type in RPN: {tok_type!r}")

    if len(stack) != 1:
        raise ValueError(f"Invalid expression: leftover stack {stack!r}")

    return stack[0]