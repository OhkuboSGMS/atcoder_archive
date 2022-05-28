from collections import deque
from itertools import product

#complete
n = int(input())
blanket = '()'


def create(n: int):
    return tuple(map(''.join, product(blanket, repeat=n)))


def valid(s, rest, stack) -> bool:
    if s == ')':
        if len(stack) == 0:
            return False
        else:
            if stack.pop() != '(':
                return False
            elif len(rest) == 0 and len(stack) == 0:
                return True
            elif len(rest) == 0:
                return False
            else:
                return valid(rest[0], rest[1:], stack)


    else:  # (
        stack.append(s)
        if len(rest) == 0:
            return False
        return valid(rest[0], rest[1:], stack)


list(map(print, tuple(filter(lambda s: valid(s[0], s[1:], deque()), create(n)))))
