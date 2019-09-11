#! /usr/bin/env python3
"""
A particular school offers cash rewards to children with good attendance and
punctuality. If they are absent for three consecutive days or late on more than
one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting
of L's (late), O's (on time), and A's (absent).

Although there are eighty-one trinary strings for a 4-day period that can be
formed, exactly forty-three strings would lead to a prize:

    OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
    OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
    AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
    AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
    LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?

Algorithm:

    Observe that any prior string must be valid, we can represent such valid
    strings by two properties - (a) whether the string does or does not contain
    a 'late'; and (b) the number of trailing 'absences', noting that this can
    be 0, 1, or 2 - since any greater number will not be a valid string.

    We can map these strings to subsequent valid strings as follows:

        (true, 0) -> (true, 0), (true, 1)
        (true, 1) -> (true, 0), (true, 2)
        (true, 2) -> (true, 0)
        (false, 0) -> (false, 0), (false, 1), (true, 0)
        (false, 1) -> (false, 0), (false, 2), (true, 0)
        (false, 2) -> (false, 0)

    This can be represented by the following transition matrix:

        [[1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 1, 0],
         [1, 0, 0, 1, 0, 1],
         [1, 0, 0, 1, 0, 0],

    So the number of valid states can be recursively calculated from the
    previous set right-multiplied by the above matrix.

Solution: 1918080160
"""
def calculate_prize_strings(n):
    """
    >>> calculate_prize_strings(4)
    43

    >>> calculate_prize_strings(30)
    1918080160
    """
    def calculate_prize_strings_array(n):
        if n == 1:
            return [1, 0, 0, 1, 1, 0]
        child_strings = calculate_prize_strings_array(n - 1)
        return [sum(child_strings),
                child_strings[0],
                child_strings[1],
                sum(child_strings[3:]),
                child_strings[3],
                child_strings[4]]
    return sum(calculate_prize_strings_array(n))

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
