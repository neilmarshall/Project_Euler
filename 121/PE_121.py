#! /usr/bin/env python3.7
"""
A bag contains one red disc and one blue disc. In a game of chance a player
takes a disc at random and its colour is noted. After each turn the disc is
returned to the bag, an extra red disc is added, and another disc is taken at
random.

The player pays £1 to play and wins if they have taken more blue discs than red
discs at the end of the game.

If the game is played for four turns, the probability of a player winning is
exactly 11/120, and so the maximum prize fund the banker should allocate for
winning in this game would be £10 before they would expect to incur a loss. Note
that any payout will be a whole number of pounds and also includes the original
£1 paid to play the game, so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which
fifteen turns are played.

Solution: 2269
"""
from fractions import Fraction

def PE121(turns):
    """
    >>> PE121(4)
    10

    >>> PE121(15)
    2269
    """
    current_paths = [(Fraction(1, 1), 1, 1, 0, 0)]    # a list of tuples of the form (prob. of winning, blue discs, red discs, blue count, red count)

    for turn in range(turns):
        new_paths = []
        for path in current_paths:
            new_paths.append((path[0] * path[1] / (path[1] + path[2]), path[1], path[2] + 1, path[3] + 1, path[4]))
            new_paths.append((path[0] * path[2] / (path[1] + path[2]), path[1], path[2] + 1, path[3], path[4] + 1))
        current_paths = new_paths
            
    probability_of_winning = sum(path[0] for path in current_paths if path[3] > path[4])

    return int(1 / probability_of_winning)


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
