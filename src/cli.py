from . import evaluate

def repl():
    while True:
        try:
            eqn = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break

        if not eqn:
            continue

        if eqn.lower() in {"quit", "exit"}:
            print("Thanks for using the math string parser")
            break

        trace = False
        expr = eqn

        if eqn.lower().startswith("trace "):
            trace = True
            expr = eqn[6:].strip()

        try:
                print(evaluate(expr, trace=trace))

        except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    repl()