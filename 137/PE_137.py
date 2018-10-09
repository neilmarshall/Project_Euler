"""
Consider the infinite polynomial series AF(x) = x.F1 + x^2.F2 + x^3.F3 + ...,
where Fk is the kth term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ;
that is, Fk = Fk−1 + Fk−2, F1 = 1 and F2 = 1.

For this problem we shall be interested in values of x for which AF(x) is a
positive integer.

The corresponding values of x for the first five natural numbers are:

    x               AF(x)
    √2 − 1          1
    1 / 2           2
    (√13 − 2) / 3   3
    (√89 − 5) / 8   4
    (√34 − 3) / 5   5

We shall call AF(x) a golden nugget if x is rational, because they become
increasingly rarer; for example, the 10th golden nugget is 74049690.

Find the 15th golden nugget.

Solution: 1120149658760
"""

def golden_nugget(n):
    """
    >>> golden_nugget(1)
    2
    
    >>> golden_nugget(10)
    74049690

    >>> golden_nugget(15)
    1120149658760
    """
    fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
    return fib(2 * n) * fib(2 * n + 1)


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
