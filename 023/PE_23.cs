/*
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.

Pseudocode solution:

    1. Define Limit = 28123
    
    2. Create an ordered list of all abundant numbers less than Limit
    
    3. Create a map of all numbers between 1 and Limit indicating whether they
       can be written as the sum of two abundant numbers - initialise all
       entries as 'false'
    
    4. For the cross-product of all abundant numbers created in step 2, while
       the sum is less than Limit mark the indicator map created in step 3
       as 'true'
    
    5. Return the sum of all numbers marked in the indicator map created in
       step 3 as 'false'

Solution: 4179871
*/

using System;
using System.Collections.Generic;

class Program
{
    private static bool isAbundant(int n)
    {
        int divisor_sum = 0;
        for (int p = 1; p <= n / 2; p++)
        {
            if (n % p == 0)
                divisor_sum += p;
        }
        return divisor_sum > n;
    }

    private static List<int> getAbundantNumbers(int n)
    {
        List<int> abundant_numbers = new List<int>();
        for (int i = 1; i <= n; i++)
        {
            if (isAbundant(i))
                abundant_numbers.Add(i);
        }
        return abundant_numbers;
    }

    public static void Main()
    {
        const int LIMIT = 28123;

        List<int> abundant_numbers = getAbundantNumbers(LIMIT);

        Dictionary<int, bool> abundant_sum_flags = new Dictionary<int, bool>();
        for (int i = 1; i <= LIMIT; i++)
            abundant_sum_flags.Add(i, false);

        foreach (int i in abundant_numbers)
        {
            foreach (int j in abundant_numbers)
            {
                if (i + j > LIMIT)
                    break;
                abundant_sum_flags[i + j] = true;
            }
        }

        int non_abundant_number_sum = 0;
        for (int i = 1; i <= LIMIT; i++)
        {
            if (!abundant_sum_flags[i])
                non_abundant_number_sum += i;
        }

        Console.WriteLine(non_abundant_number_sum);
    }
}
