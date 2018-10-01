"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from string import ascii_uppercase

class Name_Scorer():

    def __init__(self, fname):
        self.letter_scores = {c: i for i, c in enumerate(ascii_uppercase, 1)}
        with open(fname, 'r') as f:
            self.names = sorted(map(lambda s: s.replace('"', ''), f.readline().split(',')))

    def _score_name(self, name):
        return sum(self.letter_scores[c] for c in name)

    def score_names(self):
        return sum(i * self._score_name(name) for i, name in enumerate(self.names, 1))


def PE_22():
    """
    >>> PE_22()
    871198282
    """
    name_scorer = Name_Scorer("p022_names.txt")
    return name_scorer.score_names()

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
