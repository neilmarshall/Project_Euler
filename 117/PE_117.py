#!/usr/bin/env python3.6

"""
Using a combination of black square tiles and oblong tiles chosen from: red
tiles measuring two units, green tiles measuring three units, and blue tiles
measuring four units, it is possible to tile a row measuring five units in
length in exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?

Solution: 100808458960497
"""
def count_substitutions(number_of_tiles):
    """
    >>> count_substitutions(50)
    100808458960497
    """
    substitutions = [[0 for i in range(5)] for _ in range(number_of_tiles + 1)]
    for r in range(number_of_tiles + 1):
        substitutions[r][0] = 1
    for r in range(2, number_of_tiles + 1):
        for c in range(2, 5):
            if c > r:
                continue
            substitutions[r][c] = sum(substitutions[x][y] for x in range(r - c + 1) for y in range(5))
    return sum(substitutions[number_of_tiles])


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
