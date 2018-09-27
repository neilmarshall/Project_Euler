import unittest

def load_grid(filename):
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            grid.append(list(map(int, line.split(' '))))
    return grid


def solve(t):
    """Find the maximal path total from top to bottom of a given triangle"""
    if len(t) == 1:
        return t[0][0]
    t[-2] = [t[-2][j] + max(t[-1][j], t[-1][j+1]) for j in range(len(t[-2]))]
    return solve(t[:-1])


class TestSolutionToProblem(unittest.TestCase):
    def test_solution_to_problem(self):
        grid = load_grid("p067_triangle.txt")
        self.assertEqual(solve(grid), 7273)

  
if __name__ == '__main__':
    unittest.main()
