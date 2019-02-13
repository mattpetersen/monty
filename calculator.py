import re


NUMERICAL_VALUE = r'\d+(?:\.\d+)?'
PARENTHETICAL_EXPRESSION =  r'\(.+\)'
OPERATIONS = ('**', '*', '/', '+', '-')


def collapse_all_math(string: str) -> str:
    string = normalize_whitespace(string)
    match = re.match('.*', string)
    return _collapse_all_math(match)


def _collapse_all_math(match: re.match) -> str:
    string = re.sub(
        PARENTHETICAL_EXPRESSION,
        _collapse_all_math,
        match.group(0)
    )
    for operation in OPERATIONS:
        string = re.sub(
            binary_operation_regex(operation),
            maybe_compute_binary_operation,
            string
        )
    return string


def maybe_compute_binary_operation(match: re.match) -> str:
    if match:
        a, operation, b = match.groups()
        a, b = float(a), float(b)
        if operation == '**': result = a ** b
        elif operation == '*': result = a * b
        elif operation == '/': result = a / b
        elif operation == '+': result = a + b
        elif operation == '-': result = a - b
        else: raise ValueError(f'Unrecognized operation: {operation}')
    else:
        result = match.group(0)
    return maybe_simplify(result)


def maybe_simplify(maybe_number: str) -> str:
    try:
        maybe_number = float(maybe_number)
        maybe_number = int(maybe_number)
    except ValueError:
        pass
    finally:
        return str(maybe_number)


def simplify(string):
    try:
        string = float(string)
        string = int(string)
    except ValueError:
        pass
    finally:
        return str(string)


def binary_operation_regex(operation: str) -> str:
    return f'({NUMERICAL_VALUE}) ({re.escape(operation)}) ({NUMERICAL_VALUE})'


def normalize_whitespace(string: str) -> str:
    return re.sub('[\s\n]+', ' ', string)

