from .tokenizer import tokenize
from .parser import to_rpn
from .evaluator import eval_rpn

def evaluate(expr: str, trace: bool = False) -> float:
    tokens = tokenize(expr)
    rpn = to_rpn(tokens)

    if trace:
        print("\nTOKENS:")
        print(tokens)
        print("\nRPN:")
        print(rpn)
        print("\nEVAL TRACE:")

    result = eval_rpn(rpn, trace=trace)

    if trace:
        print(f"\nRESULT: {result}\n")

    return result