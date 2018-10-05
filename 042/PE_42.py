"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?

Solution: 162
"""

from string import ascii_uppercase

def score_word(word, scorer):
    return sum(scorer.get(c, 0) for c in word)


def is_triangle_number(n):
    """Check n is an integer root of the equation x^2 + x - 2n"""
    root = (-1 + (1 + 8 * n)**0.5) / 2
    return int(root) * (int(root) + 1) / 2 == n


def PE_42():
    """
    >>> PE_42()
    162
    """
    with open("p042_words.txt", 'r') as f:
        words = f.readlines()[0].split(',')
    scorer = {c: i for i, c in enumerate(ascii_uppercase, 1)}
    return len(list(filter(is_triangle_number, (score_word(word, scorer) for word in words))))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
