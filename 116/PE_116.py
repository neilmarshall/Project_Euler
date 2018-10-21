#!/usr/bin/env python3.6

"""
A row of five black square tiles is to have a number of its tiles replaced with
coloured oblong tiles chosen from red (length two), green (length three), or
blue (length four).

If red tiles are chosen there are exactly seven ways this can be done. If green
tiles are chosen there are three ways, and if blue tiles are chosen there are
two ways.

Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing
the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty units in
length be replaced if colours cannot be mixed and at least one coloured tile
must be used?

Solution: 20492570929
"""
def substitutions_using_tiles_of_one_color(total_tiles, color_length):
    substitutions = [[0 for i in range(total_tiles // color_length + 1)] for _ in range(total_tiles + 1)]
    for r in range(color_length, total_tiles + 1):
        substitutions[r][1] = r - color_length + 1
    for c in range(2, total_tiles // color_length + 1):
        for r in range(color_length * c, total_tiles + 1):
            substitutions[r][c] = sum(substitutions[i][c - 1] for i in range(color_length * (c - 1), r - color_length + 1))
    return sum(substitutions[total_tiles])


def count_substitutions(number_of_tiles):
    """
    >>> count_substitutions(50)
    20492570929
    """
    return sum(map(lambda n: substitutions_using_tiles_of_one_color(number_of_tiles, n), (2, 3, 4)))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
