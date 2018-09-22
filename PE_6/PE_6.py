"""
The sum of the squares of the first ten natural numbers
is 1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers
is (1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum
is 3025 - 385 = 2640.

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of
the sum.
"""

def PE_6(limit):
    """
    >>> PE_6(10)
    2640

    >>> PE_6(100)
    25164150
    """
    squareSum = sumSquare = 0
    for i in range(1, limit + 1):
        squareSum += i**2
        sumSquare += i
    return sumSquare**2 - squareSum


if __name__ == '__main__':
    import doctest; doctest.testmod()
