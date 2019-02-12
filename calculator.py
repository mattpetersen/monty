from collections import deque
import re
from typing import *


def apply_operation(a: str, b: str, op: str) -> str:
    a, b = float(a), float(b) 
    if op == '**': return str(a ** b)
    elif op == '*': return str(a * b)
    elif op == '/': return str(a / b)
    elif op == '+': return str(a + b)
    elif op == '-': return str(a - b)
    else: raise ValueError(f'Unrecognized operation {op}')


def calculate(message: str) -> Union[int, float]:
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
    try:
        return int(message)
    except ValueError:
        try:
            return float(message)
        except ValueError:
            return message

