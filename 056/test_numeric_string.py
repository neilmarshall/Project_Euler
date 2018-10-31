#! venv/bin/python3.7
import unittest

from PE_56 import NumberAsString

class NumberAsStringInitialisedFromZero(unittest.TestCase):
    def setUp(self):
        self.n0 = NumberAsString()

    def test_str_method_returns_zero_as_string(self):
        self.assertEqual(str(self.n0), "0")

    def test_rep_method_returns_valid_string_representation(self):
        self.assertEqual(repr(self.n0), "NumberAsString('0')")

    def test_len_method_returns_1(self):
        self.assertEqual(len(self.n0), 1)


class NumberAsStringInitialisedFromString(unittest.TestCase):
    def setUp(self):
        self.n123 = NumberAsString("123")

    def test_str_method_returns_123_as_string(self):
        self.assertEqual(str(self.n123), "123")

    def test_rep_method_returns_valid_string_representation(self):
        self.assertEqual(repr(self.n123), "NumberAsString('123')")

    def test_len_method_returns_3(self):
        self.assertEqual(len(self.n123), 3)


class NumberAsStringInitialisedFromNonStringArgument(unittest.TestCase):
    def test_constructor_throws_if_invalid_argument_passed(self):
        self.assertRaises(TypeError, NumberAsString, 123)


class NumberAsStringAddMethod(unittest.TestCase):
    def setUp(self):
        self.n0 = NumberAsString()
        self.n123 = NumberAsString("123")
        self.n9999 = NumberAsString("9999")

    def test_zero_plus_zero_returns_zero(self):
        self.assertEqual(self.n0 + self.n0, NumberAsString())

    def test_zero_plus_123_returns_123(self):
        self.assertEqual(self.n0 + self.n123, NumberAsString("123"))

    def test_123_plus_123_returns_246(self):
        self.assertEqual(self.n123 + self.n123, NumberAsString("246"))

    def test_123_plus_9999_returns_10122(self):
        self.assertEqual(self.n123 + self.n9999, NumberAsString("10122"))


class NumberAsStringMulMethod(unittest.TestCase):
    def setUp(self):
        self.n0 = NumberAsString()
        self.n1 = NumberAsString("1")
        self.n3 = NumberAsString("3")
        self.n27 = NumberAsString("27")
        self.n123 = NumberAsString("123")
        self.n9999 = NumberAsString("9999")

    def test_zero_times_zero_is_zero(self):
        self.assertEqual(self.n0 * self.n0, NumberAsString())

    def test_zero_times_1_is_zero(self):
        self.assertEqual(self.n0 * self.n1, NumberAsString())

    def test_1_times_1_is_1(self):
        self.assertEqual(self.n1 * self.n1, NumberAsString("1"))

    def test_1_times_123_is_123(self):
        self.assertEqual(self.n1 * self.n123, NumberAsString("123"))

    def test_123_times_123_is_15129(self):
        self.assertEqual(self.n123 * self.n123, NumberAsString("15129"))

    def test_3_times_27_is_81(self):
        self.assertEqual(self.n3 * self.n27, NumberAsString("81"))

    def test_27_times_3_is_81(self):
        self.assertEqual(self.n27 * self.n3, NumberAsString("81"))

class NumberAsStringPowMethod(unittest.TestCase):
    def setUp(self):
        self.n3 = NumberAsString("3")
        self.n4 = NumberAsString("4")

    def test_3_raised_to_power_4_is_81(self):
        self.assertEqual(self.n3**self.n4, NumberAsString("81"))


if __name__ == '__main__':
    unittest.main()
