/**
Project Euler # 30: Digit fifth powers
--------------------------------------
Problem
-------
Surprisingly there are only three numbers that can be written
as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum
of fifth powers of their digits.

Solution
--------
If we have a number with n digits, then the maximum value of the
digit powers for power k is n x 9^k.

A number with n digits is at least 10^(n - 1).

So the largest number of digits that we can have to satisfy the
equation is given by MAX{ n | n x 9^k >= 10^(n - 1) }

Hence we first define this limit.

The next step is then to check all numbers up to this limit, and
return the sum of those that satisfy the problem.

Note that we start the check from 10, as single digit numbers are
not considered valid solutions to the problem.

Test cases:
    Solution for k = 4: 19,316
    Solution for k = 5: 443,839
*/

using System;

class Program {

    static int get_limit(int k) {
        int n = 1;
        while (n * (int)Math.Pow(9, k) >= (int)Math.Pow(10, n - 1)) n += 1;
        return (n - 1) * (int)Math.Pow(9, k);
    }
    
    static bool check_candidate(int candidate, int k) {
        int power_digit_sum = 0;
        string s = Convert.ToString(candidate);
        for (int i = 0; i < s.Length; ++i) {
            power_digit_sum += (int)Math.Pow((int)Char.GetNumericValue(s[i]), k);
        }
        return power_digit_sum == candidate;
    }
    
    static int sum_of_digit_power_sums(int k) {
        int limit = get_limit(k);
        int sum = 0;
        for (int n = 2; n <= limit; n++) {
            if (check_candidate(n, k)) sum += n;
        }
        return sum;
    }
    
    static void Main() {

    Console.WriteLine("Solution for k = 4: " + sum_of_digit_power_sums(4));
    Console.WriteLine("Solution for k = 5: " + sum_of_digit_power_sums(5));

  }

}
