"""
Each of the six faces on a cube has a different digit (0 to 9) written on it; the
same is done to a second cube. By placing the two cubes side-by-side in different
positions we can form a variety of 2-digit numbers.

In fact, by carefully choosing the digits on both cubes it is possible to display
all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one
cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that
an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine
square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube,
not the order.

    {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
    {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last
example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of
forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers
to be displayed?

Solution: 1217
"""
from itertools import combinations, product

def PE_90():
    """
    >>> PE_90()
    1217
    """

    solution_count = 0

    sets = list(combinations(range(10), 6))
    
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            setA, setB = sets[i], sets[j]
            if all_squares_present(setA, setB):
                solution_count += 1

    return solution_count


def all_squares_present(setA, setB):
    """
    >>> all_squares_present((0, 5, 6, 7, 8, 9), (1, 2, 3, 4, 8, 9))
    True

    >>> all_squares_present((0, 5, 6, 7, 8, 9), (1, 2, 3, 4, 6, 7))
    True
    """
    if 6 in setA and 9 not in setA:
        setA = list(setA) + [9]
    if 6 in setB and 9 not in setB:
        setB = list(setB) + [9]
    if 9 in setA and 6 not in setA:
        setA = list(setA) + [6]
    if 9 in setB and 6 not in setB:
        setB = list(setB) + [6]

    digits = set(int(str(a) + str(b)) for a, b in product(setA, setB)).union(set(int(str(b) + str(a)) for a, b in product(setA, setB)))
    return all(square in digits for square in (1, 4, 9, 16, 25, 36, 49, 64, 81))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
