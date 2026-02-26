"""
Parses through the tokenized list implementing the Shunting Yard algorthim
to convert the tokens to RPN. Handling order of operations for later evaluation.
"""

PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2,"^": 3,"NEG" : 4}
RIGHT_ASSOC = {"^","NEG"}

def prec(op: str) -> int:
    return PRECEDENCE[op]

def to_rpn(tokens: list[tuple[str, str | float | int]]) -> list[tuple[str, str | float | int]]:
    out: list[tuple[str,object]] = []
    op_stack: list[tuple[str,object]] = []
    
    for t, v in tokens:
        match t:
            case "NUM":
                out.append((t,v))

            case "OP":
                while (
                    op_stack
                    and op_stack[-1][0] == "OP"
                    and (
                        prec(op_stack[-1][1]) > prec(v)
                        or (prec(op_stack[-1][1]) == prec(v) and v not in RIGHT_ASSOC)
                    )
                ):
                    out.append(op_stack.pop())    
                op_stack.append((t,v))

            case "LPAREN":
                op_stack.append((t,v))

            case "RPAREN":
                while op_stack and  op_stack[-1][0] != 'LPAREN':
                    out.append(op_stack.pop())

                if not op_stack:
                    raise ValueError("Mismatched parentheses")
                
                op_stack.pop()

            case _:
                raise ValueError(f"Unknown token type {t!r}")

    while op_stack:
        if op_stack[-1][0] == 'LPAREN':
            raise ValueError("Mismatched parentheses")
        
        out.append(op_stack.pop())

    return out