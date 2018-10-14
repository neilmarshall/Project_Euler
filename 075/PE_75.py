#! venv/bin/python3

"""
It turns out that 12cm is the smallest length of wire that can be bent to form
an integer sided right angle triangle in exactly one way, but there are many
more examples.

    12cm: (3,4,5)
    24cm: (6,8,10)
    30cm: (5,12,13)
    36cm: (9,12,15)
    40cm: (8,15,17)
    48cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
integer sided right angle triangle, and other lengths allow more than one
solution to be found; for example, using 120 cm it is possible to form exactly
three different integer sided right angle triangles.

    120cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can
exactly one integer sided right angle triangle be formed?

Solution: 161667
"""

from collections import defaultdict
from itertools import count

from pyutils.pythagorean_triples import PythagoreanTripleGenerator

def main():

    LIMIT = 1500000

    length_count_map = defaultdict(int)  # holds count of number of triples indexed by perimeter length

    ptg = PythagoreanTripleGenerator()

    # for each primitive triple ...
    while (True):
        a, b, c = ptg.GetNextTriple()
        if (a + b + c > LIMIT):
            break

        # for each multiple of each primitive triple ...
        for n in count(1):
            length = n * (a + b + c)
            if (length > LIMIT):
                break
            length_count_map[length] += 1

    # cycle through map of perimeter counts and return count of the number equal to 1
    return list(length_count_map.values()).count(1)


if __name__ == '__main__':
    print(main())

