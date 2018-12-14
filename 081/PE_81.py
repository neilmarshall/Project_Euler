#! /usr/bin/env python3.7
"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is equal to 2427.

    [[131, 673, 234, 103, 18],
     [201, 96, 342, 965, 150],
     [630, 803, 746, 422, 111],
     [537, 699, 497, 121, 956],
     [805, 732, 524, 37, 331]]

Find the minimal path sum in p081_matrix.txt from the top left to the bottom
right by only moving right and down.

Solution: 427337
"""
import unittest

def parse_input_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.split(','))) for line in file]
    return matrix


def solve(matrix):
    for r in range(1, len(matrix) * 2- 1):
        c = 0
        while c < len(matrix) and r >= 0:
            if r < len(matrix):
                if r - 1 >= 0 and c - 1 >= 0:
                    addition = min(matrix[r - 1][c], matrix[r][c - 1])
                elif r - 1 >= 0:
                    addition = matrix[r - 1][c]
                elif c - 1 >= 0:
                    addition = matrix[r][c - 1]
                else:
                    addition = 0
                matrix[r][c] += addition
            r -= 1
            c += 1
    return matrix[-1][-1]


class TestPE77(unittest.TestCase):

    def test_base_case(self):
        matrix = [[131, 673, 234, 103, 18],
                  [201, 96, 342, 965, 150],
                  [630, 803, 746, 422, 111],
                  [537, 699, 497, 121, 956],
                  [805, 732, 524, 37, 331]]
        self.assertEqual(solve(matrix), 2427)
    
    def test_PE77(self):
        matrix = parse_input_file("p081_matrix.txt")
        self.assertEqual(solve(matrix), 427337)


if __name__ == '__main__':
    unittest.main()
