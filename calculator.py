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

