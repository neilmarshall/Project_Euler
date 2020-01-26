#! venv/bin/python3

from concurrent.futures import ProcessPoolExecutor
from nmutils.miller_rabin import MillerRabin

def t_is_prime(n):
    return MillerRabin().is_prime(2 * n**2 - 1)

def PE(n):
    """
    >>> PE(10_000)
    2202
    """
    with ProcessPoolExecutor() as ppe:
        return sum(1 for x in ppe.map(t_is_prime, range(2, n + 1)) if x)

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
    print(PE(50_000_000))
