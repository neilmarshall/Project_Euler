"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and
each line adding to nine.

       4
        \
         \
          3
         / \
        /   \
       1-----2-----6
      /
     /
    5

Working clockwise, and starting from the group of three with the numerically
lowest external node (4,3,2 in this example), each solution can be described
uniquely. For example, the above solution can be described by the
set {4,3,2; 6,2,1; 5,1,3}.

It is possible to complete the ring with four different totals: 9, 10, 11, and
12. There are eight solutions in total:

    Total    Solution set
     9       4,2,3; 5,3,1; 6,1,2
     9       4,3,2; 6,2,1; 5,1,3
    10       2,3,5; 4,5,1; 6,1,3
    10       2,5,3; 6,3,1; 4,1,5
    11       1,4,6; 3,6,2; 5,2,4
    11       1,6,4; 5,4,2; 3,2,6
    12       1,5,6; 2,6,4; 3,4,5
    12       1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum
string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form
16- and 17-digit strings. What is the maximum 16-digit string for a "magic"
5-gon ring?

Solution: 6531031914842725
"""
from itertools import product

def PE_68():
    """
    There are 10 x 5 x 4 = 120 options for the first 3-node set
    There are 3 x 2 x 1 = 10 options for the second 3-node set
    There are 1 x 1 x 1 = 1 options for the third 3-node set
    So there are 120 x 10 x 1 = 720 total options
    Check each to see if test condition holds, and if so add result to output

    >>> PE_68()
    6531031914842725
    """
    astrOutput = []
    for a, b, c in product(range(1, 11), repeat=3):
        if a != b and a != c and b != c:
            for e, d in product(range(1, 11), repeat=2):
                if d not in {a, b, c} and e not in {a, b, c} and d != e and sum((a, b, c)) == sum((c, d, e)):
                    for f, g in product(range(1, 11), repeat=2):
                        if f not in {a, b, c, d, e} and g not in {a, b, c, d, e} and f != g and sum((a, b, c)) == sum((e, f, g)):
                            for h, i in product(range(1, 11), repeat=2):
                                if h not in {a, b, c, d, e, f, g} and i not in {a, b, c, d, e, f, g} and h != i and sum((a, b, c)) == sum((g, h, i)):
                                    for j in range(1, 11):
                                        if j not in {a, b, c, d, e, f, g, h, i} and sum((a, b, c)) == sum((b, i, j)):
                                            strOutput = ''.join(map(str, (a, b, c, d, c, e, f, e, g, h, g, i, j, i, b)))
                                            if not_a_rotation(strOutput, astrOutput):
                                                astrOutput.append(strOutput)
    return int(astrOutput[-1])


def not_a_rotation(string, known_strings):
    for known_string in known_strings:
        if are_rotations(string, known_string):
            return False
    return True


def are_rotations(string1, string2):
    if len(string1) != len(string2):
        return False
    for _ in range(len(string1)):
        string2 = string2[1:] + string2[0]
        if string1 == string2:
            return True
    return False


if __name__ == '__main__':
    import doctest; doctest.testmod()
