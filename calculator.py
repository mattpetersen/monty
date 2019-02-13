from collections import deque
import re


def clean(number: str) -> str:
    try:
        number = float(number)
        number = int(number)
    except ValueError:
        pass
    return str(number)


def apply_operation(a: str, b: str, op: str) -> str:
    a, b = float(a), float(b)
    if op == '**': result = a ** b
    elif op == '*': result = a * b
    elif op == '/': result = a / b
    elif op == '+': result = a + b
    elif op == '-': result = a - b
    else: raise ValueError(f'Unrecognized operation {op}')
    return clean(result)


def calculate(message: str) -> str:
    """Return message after replacing any math syntax with its result."""

    parens = re.search(r'\(.+\)', message)
    while parens:
        message = (
            message[:parens.start()]
            + calculate(parens.group(0).strip('()'))
            + message[parens.end():]
        )
        parens = re.search(r'\(.+\)', message)

    number = r'\d+(?:\.\d+)?'
    operations = deque(['-', '+', '/', '*', '**'])
    message = re.sub('[\s\n]+', ' ', message)
    while operations:
        operation = operations.pop()
        regex = f'({number}) {re.escape(operation)} ({number})'
        search = re.search(regex, message)
        while search:
            message = (
                message[:search.start()]
                + apply_operation(*search.groups(), operation)
                + message[search.end():]
            )
            search = re.search(regex, message)
    return message

