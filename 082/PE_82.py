#! /usr/bin/env python3.7
"""
Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 
matrix, from the left column to the right column.

Solution: 260324
"""
import unittest

def solve(M, verbose=False):
    """
    >>> M = [[234,103,18],[342,965,150],[746,422,111]]
    >>> solve(M)
    355
    
    >>> M = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],\
             [537,699,497,121,956],[805,732,524,37,331]]
    >>> solve(M)
    994
    """
    def rows_to_columns(M):
        return [[M[r][c] for r in range(len(M))] for c in range(len(M))]
    def reduce_to_distances(M):  # convert a matrix to a single list representing minimum distances from the first column to the last
        def combine(A, B):  # helper function to merge two columns into one
            def f(A, B):  # generator used by 'combine' function
                prev = A[0] + B[0]
                yield prev
                for i in range(1, len(A)):
                    prev = A[i] + min(B[i], prev)
                    yield prev
            return list(map(min, zip(f(A, B), reversed(list(f(list(reversed(A)), list(reversed(B))))))))
        if len(M) == 1:  # base case
            return M[0]
        if len(M) == 2:  # recursive case(s)
            return combine(M[-2], M[-1])
        return reduce_to_distances(M[:-2] + [combine(M[-2], M[-1])])
    return min(reduce_to_distances(rows_to_columns(M)))


class TestSolve(unittest.TestCase):
    def test_3_by_3_matrix(self):
        M = [[234,103,18],[342,965,150],[746,422,111]]
        self.assertEqual(solve(M), 355)
    
    def test_5_by_5_matrix(self):
        M = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],\
             [537,699,497,121,956],[805,732,524,37,331]]
        self.assertEqual(solve(M), 994)

    def test_80_by_80_matrix(self):
        with open("p082_matrix.txt") as f:
            M = [list(map(int, line.split(','))) for line in f]
        self.assertEqual(solve(M), 260324)


if __name__ == '__main__':
    unittest.main()
