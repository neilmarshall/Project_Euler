import doctest

from pyutils import primes
from pyutils import pythagorean_triples

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(primes))
    tests.addTests(doctest.DocTestSuite(pythagorean_triples))
    return tests

