#! venv/bin/python3.7
"""
Considering 4-digit primes containing repeated digits it is clear that they
cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and
so on. But there are nine 4-digit primes containing three ones:

    1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated digits for
an n-digit prime where d is the repeated digit, N(n, d) represents the number of
such primes, and S(n, d) represents the sum of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime
where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum
of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is only
possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such
cases.

For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).

Solution: 612407567715
"""
from math import sqrt

from pyutils.primes import is_prime, get_primes_under_n

def S(characters):
    """
    >>> S(4)
    273700

    >>> S(10)
    612407567715
    """
    upper_limit = int(characters * '9')
    lower_limit = int('1' + (characters - 1) * '0')
    primes = get_primes_under_n(int(sqrt(upper_limit)))
    p = primes[-1] + 1
    while not is_prime(p):
        p += 1
    primes.append(p)

    M = [0 for i in range(10)]
    N = [0 for i in range(10)]
    S = [0 for i in range(10)]
    all_primes = set()

    def record_statistics(n, d, repeats):
        M[d] = repeats
        N[d] += 1
        S[d] += n
        all_primes.add(n)
        
    def check_candidates(candidates, d, repeats):
        for candidate in candidates:
            if int(candidate) not in all_primes:        
                if int(candidate) < lower_limit:
                    continue
                if is_prime(int(candidate), primes):
                    record_statistics(int(candidate), d, repeats)
      
    # check for 'characters - 1' repeated digits, excluding zero  
    for d in range(1, 10):
        for n in range(10):
            if d == n:
                continue
            s = (characters - 1) * str(d) + str(n)
            candidates = [s]        
            for i in range(characters - 1, 0, -1):
                s = s[:i - 1] + s[i] + s[i - 1] + s[i + 1:]
                candidates.append(s)
            check_candidates(candidates, d, characters - 1)

    # check for 'characters - 2' repeated digits, excluding zero  
    for d in [m for m in range(10) if M[m] is 0]:
        for n in range(10):    
            if n == d:
                continue
            candidates = []
            for i in range(0, characters - 1):        
                s = (characters - 2 - i) * str(d) + 2 * str(n) + i * str(d)
                candidates.append(s)
                for j in range(characters - 2 - i, 0, -1):
                    s = s[:j - 1] + s[j] + s[j - 1] + s[j + 1:]
                    candidates.append(s)
            for c in range(sum([x for x in range(characters)])):
                i = len(candidates[c]) - 1            
                while candidates[c][i] == str(d):
                    i -= 1
                for j in range(10):
                    if j != d:
                        s = candidates[c][:i] + str(j) + candidates[c][i + 1:]
                        candidates.append(s)
            check_candidates(candidates, d, characters - 2)

    return sum(S)


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
