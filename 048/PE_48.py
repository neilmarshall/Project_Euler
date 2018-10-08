"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def PE_48():
    """
    >>> PE_48()
    9110846700
    """
    def raise_to_self_power_and_restrict_length(n):
        return int(str(n**n)[-10:])
    return int(str(sum(raise_to_self_power_and_restrict_length(n) for n in range(1, 1000)))[-10:])

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
