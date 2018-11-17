#! venv/bin/python3.7
"""
Consider quadratic Diophantine equations of the form:

    x^2 – D.y^2 = 1

For example, when D = 13, the minimal solution in x is 649^2 – 13 x 180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

    3^2 – 2 x 2^2 = 1
    2^2 – 3 x 1^2 = 1
    9^2 – 5 x 4^2 = 1
    5^2 – 6 x 2^2 = 1
    8^2 – 7 x 3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
obtained when D = 5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest 
value of x is obtained.

Solution: 661
"""
from pyutils.sqrt_expansion import SqrtExpansion

def solve_for_D(D):
    """
    >>> solve_for_D(23)
    24

    >>> solve_for_D(998)
    984076901
    """
    try:
        expansion = SqrtExpansion(D)
    except ValueError:
        return 0
    h0, h1 = expansion.root, 1
    k0, k1 = 1, 0
    count = 0
    while True:
        if h0**2 == D * k0**2 + 1:
            return h0
        coefficient = expansion.coefficient(count)
        count += 1
        h0, h1 = coefficient * h0 + h1, h0
        k0, k1 = coefficient * k0 + k1, k0


def PE_66():
    """
    >>> PE_66()
    661
    """
    return max(range(2, 1001), key=solve_for_D)


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
