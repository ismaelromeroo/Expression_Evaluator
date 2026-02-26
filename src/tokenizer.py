"""
Tokenizes a mathematical expression string into structured tokens.
Handles integers, floats, basic operators, unary minus, and parentheses.
Converts raw string characters into meaningful data types used for evaluation.
"""

def tokenize(expr: str) -> list[tuple[str, str | float | int]]:
    tokens: list[tuple[str, str | float | int]] = []
    i = 0

    while i < len(expr):
        ch = expr[i]

        if ch.isspace():
            i +=1
            continue

        if ch.isdigit() or ch == ".":
            seen_dot = False
            start = i

            while i < len(expr):
                if expr[i].isdigit():
                    i+=1
                elif expr[i] == "." and not seen_dot:
                    seen_dot = True
                    i+=1
                else:
                    break

            num_val = expr[start:i]

            if num_val == ".":
                raise ValueError("Invalid number")
            
            if i < len(expr) and expr[i] == ".":
                raise ValueError("Invalid number format")

            tokens.append(("NUM", float(num_val) if seen_dot else int(num_val)))
            continue

        match ch:
            case "(":
                tokens.append(("LPAREN", ch))

            case ")":
                tokens.append(("RPAREN", ch))

            case "-":
                if (not tokens) or (tokens[-1][0] in {"OP", "LPAREN"}):
                    tokens.append(("OP", "NEG"))

                else:
                    tokens.append(("OP", "-"))

            case "+" | "*" | "/" | "^":
                tokens.append(("OP", ch))

            case _:
                raise ValueError(f'Unexpected character {ch!r} at position {i} in {expr!r}')

        i+=1

    return tokens