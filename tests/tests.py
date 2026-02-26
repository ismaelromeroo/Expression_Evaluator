from src import evaluate


def approx_equal(a, b, tol=1e-9):
    return abs(a - b) < tol


def assert_raises(expr: str, exc_type=Exception):
    try:
        evaluate(expr)

    except exc_type:
        return
    
    except Exception as e:
        raise AssertionError(f"{expr!r}: expected {exc_type.__name__}, got {type(e).__name__}: {e}") from e
    
    else:
        raise AssertionError(f"{expr!r}: expected {exc_type.__name__}, but no error was raised")

def run_tests():
    cases = [
        ("0", 0),
        ("2+2", 4),
        ("10-3", 7),
        ("2*3", 6),
        ("8/4", 2),

        (" 2 + 6 / 2 ", 5),
        ("\t2*(3+4)\n", 14),

        ("2+3*4", 14),
        ("2*3+4", 10),
        ("18/3/3", 2),
        ("10-3-2", 5),

        ("(2+3)*4", 20),
        ("2*(3+4)", 14),
        ("(2+(3*4))", 14),
        ("((2+3)*((4)))", 20),

        ("-3+2", -1),
        ("2*-3", -6),
        ("-(2+1)", -3),
        ("10--3", 13),
        ("--3", 3),

        ("3.5+2", 5.5),
        (".5+.5", 1.0),
        ("10.+5", 15.0),
        ("2*3.0", 6.0),
        ("3.14*2", 6.28),

        ("2^3", 8),
        ("2^3^2", 512),
        ("(2^3)^2", 64),
        ("2^(3^2)", 512),

        ("-2^2", 4),
        ("(-2)^2", 4),
        ("-(2^2)", -4),
        ("2^-3", 0.125),
        ("2^(-3)", 0.125),
        ("(1.5+0.5)*2^3", 16.0),
    ]

    for expr, expected in cases:
        got = evaluate(expr)
        assert approx_equal(got, expected), f"{expr!r}: got {got}, expected {expected}"

    bad = [
        "",
        "   ",
        "2 +",
        "+ 2",
        "(2+3",
        "2+3)",
        "()",
        ".",
        "3.1.4",
        "5..2",
        "..5",
        "2//3",
        "2**3",
        "2^^3",
        "2 + @",
    ]

    for expr in bad:
        assert_raises(expr, Exception)

    print(f"All tests passed. ({len(cases)} valid, {len(bad)} invalid)")


if __name__ == "__main__":
    run_tests()