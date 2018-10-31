def PE_56():
    """
    >>> PE_56()  # doctest: +SKIP
    972
    """
    LIMIT = 99
    maximal_digit_sum = 0
    for a in range(1, LIMIT + 1):
        for b in range(1, LIMIT + 1):
            AexpB = exponentiate_string(a, b)  # return a**b as a string
            maximal_digit_sum = max(maximal_digit_sum, len(AexpB))
    return maximal_digit_sum


def exponentiate_string(a, b):
    """
    >>> print(exponentiate_string(2, 2))
    4
    
    >>> print(exponentiate_string(3, 4))
    81
    """
    AexpB, a = NumberAsString(), NumberAsString(str(a))
    for _ in range(b):
        AexpB += a
    return AexpB


class NumberAsString():
    def __init__(self, s=None):
        if s is not None:
            if type(s) is not str:
                raise TypeError("Argument must be nil or a string")
        self.s = s if s is not None else "0"

    def __str__(self):
        return self.s

    def __rep__(self):
        return "NumberAsString({0})".format(self.s)

    def __len__(self):
        return len(self.s)

    def __add__(self, other):
        BASE = 10
        
        LHS, RHS = self.s, other.s
        while len(LHS) < len(RHS):
            LHS = '0' + LHS
        while len(RHS) < len(LHS):
            RHS = '0' + RHS
    
        carry, result = 0, ""
        for left, right in zip(reversed(LHS), reversed(RHS)):
            n = int(left) + int(right) + carry
            carry = n // BASE
            result = str(n % BASE) + result
        if carry != 0:
            result = str(carry) + result

        return NumberAsString(result)


if __name__ == '__main__':
    import doctest; doctest.testmod()
