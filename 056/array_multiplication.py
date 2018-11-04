#! venv/bin/python3.7
from itertools import zip_longest

def array_multiplication(arr1, arr2):
    """
    >>> array_multiplication([3], [3, 4, 5, 6])
    [1, 0, 3, 6, 8]

    >>> array_multiplication([3, 4, 5, 6], [3])
    [1, 0, 3, 6, 8]

    >>> array_multiplication([1, 2, 3], [3, 4, 5, 6])
    [4, 2, 5, 0, 8, 8]
    """
    multiplicand, multiplier = min(arr1, arr2, key=len), max(arr1, arr2, key=len)
    product = []
    for i, a in enumerate(reversed(multiplicand)):
        out, carry = [0] * i, 0
        for b in reversed(multiplier):
            n = a * b + carry
            out.append(n % 10)
            carry = n // 10
        if carry:
            out.append(carry)
        product = array_addition(product, out[::-1])
    return product


def array_addition(arr1, arr2):
    """
    >>> array_addition([1, 2, 3], [3, 4, 5, 6])
    [3, 5, 7, 9]

    >>> array_addition([1, 0, 3, 6, 8], [6, 9, 1, 2, 0])
    [7, 9, 4, 8, 8]

    >>> array_addition([6, 9, 1, 2, 0], [1, 0, 3, 6, 8])
    [7, 9, 4, 8, 8]
    """
    out, carry = [], 0
    for a, b in zip_longest(reversed(arr1), reversed(arr2), fillvalue=0):
        n = a + b + carry
        out.append(n % 10)
        carry = n // 10
    return out[::-1]


if __name__ == '__main__':
    import doctest; doctest.testmod()
