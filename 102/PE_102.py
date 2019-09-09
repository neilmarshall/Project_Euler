#! /usr/bin/env python3

"""
Three distinct points are plotted at random on a Cartesian plane, for
which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

    A(-340,495), B(-153,-910), C(835,-947)

    X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas
triangle XYZ does not.

Using p102_triangles.txt, a text file containing the co-ordinates of
one thousand "random" triangles, find the number of triangles for
which the interior contains the origin.

Solution: 228
"""

from collections import namedtuple
from itertools import islice

Point = namedtuple('Point', ['x', 'y'])

def parse_points(filename):
    def parse_line(line):
        points = map(int, line.split(','))
        return tuple(Point(*islice(points, 2)) for _ in range(3))
    with open("p102_triangles.txt") as f:
        yield from map(parse_line, f)


def contains_origin(points):
    """
    >>> contains_origin((Point(x=-340, y=495), Point(x=-153, y=-910), Point(x=835, y=-947)))
    True

    >>> contains_origin((Point(x=-175, y=41), Point(x=-421, y=-714), Point(x=574, y=-645)))
    False
    """
    def check_points(a, b, c):
        m0 = a.y / a.x if a.x != 0 else 0
        mT = (c.y - b.y) / (c.x - b.x) if c.x != b.x else 0
        x = (b.y - mT * b.x) / (m0 - mT)
        return a.x <= 0 and x >= 0 or a.x >= 0 and x <= 0
    A, B, C = points
    return check_points(A, B, C) and check_points(B, C, A) and check_points(C, A, B)


def count_triangles_containing_origin(filename):
    """
    >>> count_triangles_containing_origin("p102_triangles.txt")
    228
    """
    return len(list(filter(contains_origin, parse_points(filename))))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
