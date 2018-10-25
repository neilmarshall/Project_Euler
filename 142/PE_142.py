#! venv/bin/python3.7
"""
Find the smallest x + y + z with integers x > y > z > 0 such
that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.

Solution: 1006193
"""
from funcs import check_primitive_solution

from pyutils.pythagorean_triples import PythagoreanTripleGenerator

def check_solution(upper_bound, a, b):
    gamma = 1
    while 2 * (gamma * b)**2 + (gamma * a)**2 < upper_bound:
        new_solution = check_primitive_solution(gamma * a, gamma * b)
        if new_solution is not 0:
            return min(new_solution, upper_bound)
        else:
            gamma += 1
    return None


def get_upper_bound():
    ptg = PythagoreanTripleGenerator()
    while True:
        a, b, c = ptg.GetNextTriple()
        upper_bound = check_primitive_solution(a, b)
        if upper_bound is not 0:
            return upper_bound
        upper_bound = check_primitive_solution(b, a)
        if upper_bound is not 0:
            return upper_bound


def PE_142():
    """
    Solution is obtained by checking the first primitive triple that gives a
    solution, then checking all non-primitive triples that are less than the
    upper bound to see if they give a smaller answer

    >>> PE_142()
    1006193
    """
    upper_bound = get_upper_bound()
    ptg = PythagoreanTripleGenerator()
    while True:
        a, b, c = ptg.GetNextTriple()
        if 2 * b**2 + a**2 >= upper_bound:
            break
        new_solution = check_solution(upper_bound, a, b)
        if new_solution is not None:
            upper_bound = min(upper_bound, new_solution)
        a, b = b, a
        if 2 * b**2 + a**2 >= upper_bound:
            break
        new_solution = check_solution(upper_bound, a, b)
        if new_solution is not None:
            upper_bound = min(upper_bound, new_solution)
    return upper_bound


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
