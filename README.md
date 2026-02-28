# Expression Evaluator (Shunting Yard + RPN)

It takes a math expression as a string (like '2*(3+4)') and evaluates it by implementing:

- Tokenization
- The Shunting Yard algorithm
- Reverse Polish Notation (RPN) stack evaluation
- Optional trace mode to visualize execution

# What It Supports

- Integers and floating-point numbers
- Unary minus ('-3', '2*-3', '--3')
- Nested parentheses
- Right-associative exponentiation (^)
- Proper operator precedence
- Execution trace mode
- 30+ automated test cases

# How It Works

The evaluator follows a 3-step pipeline:

Input String
↓
Tokenize
↓
Convert to RPN (Shunting Yard)
↓
Evaluate using a stack


1. Tokenization

The input string is scanned character-by-character and converted into structured tokens.

Example:

"2*(3+4)"
→
[('NUM', 2), ('OP', '*'), ('LPAREN', '('), ('NUM', 3), ('OP', '+'), ('NUM', 4), ('RPAREN', ')')]

This step also handles:
- Floating point numbers
- Unary minus detection
- Invalid number formats

2. Parsing (Shunting Yard Algorithm)

The infix expression is converted into Reverse Polish Notation (RPN).  
This removes the need to worry about operator precedence during evaluation.

Example:

2*(3+4)
→
2 3 4 + *

The implementation handles:
- Operator precedence
- Right-associative exponentiation (^)
- Unary negation
- Parentheses matching

# 3. RPN Evaluation

The RPN expression is evaluated using a stack:

- Push numbers onto the stack
- When an operator appears:
  - Pop required operands
  - Apply operation
  - Push result back

This keeps evaluation logic simple and deterministics

# Running the Project

From the project root:

Start the calculator:

py -m src.cli

Run the test suite:

py -m tests.test_core

# Trace Mode

You can see how the evaluator works internally by using trace mode:

calc> trace 2+3+4-9-(3^4)/5

Example output:

TOKENS:
[('NUM', 2), ('OP', '+'), ('NUM', 3), ...]

RPN:
[('NUM', 2), ('NUM', 3), ('OP', '+'), ...]

EVAL TRACE:
push 2 -> [2]
push 3 -> [2, 3]
2 + 3 -> 5 ; stack [5]
...
RESULT: -16.2

Trace mode prints:
- The token list
- The RPN representation
- The stack state after each operation

This helped me debug and understand the evaluation flow clearly.

# Project Structure

src/
tokenizer.py
parser.py
evaluator.py
engine.py
cli.py
tests/
test_core.py

Each module has a single responsibility:

- tokenizer.py → lexical analysis
- parser.py → Shunting Yard implementation
- evaluator.py → RPN stack execution
- engine.py → pipeline coordination
- cli.py → user interface

# Time & Space Complexity

For an input of length n:

- Tokenization: O(n)
- Shunting Yard parsing: O(n)
- RPN evaluation: O(n)

Overall time complexity: O(n)
Space complexity: O(n)

# Example Expressions

- 2+3*4
- (2+3)4
- -3 + 2
- 2-3
- 10--3
- 3.5 + 2
- .5 + .5
- 2^3^2
- (1.5+0.5)*2^3
