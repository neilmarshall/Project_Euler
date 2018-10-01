/*
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

--------------------------------------------------------------------------------

Steps taken in getting to the solution:

    1. 9! + ... + 9! = n x 9! = 362,880 x n  [where 9...9 = 10^n - 1]

    2. 362,880 x n  < 10^n - 1 when n <= 7, therefore we need only check
       numbers up to 10^7 - 1 = 9_999_999 (as larger numbers cannot possibly
       be curious)

Solution: 40730
*/

using System;

class Program
{
    private static int Fact(int n) { return n > 1 ? n * Fact(n - 1) : 1; }

    private static bool isCurious(int n)
    {
        int n0 = n, remainder;
        while (n0 > 0)
        {
            n0 = Math.DivRem(n0, 10, out remainder);
            n -= Fact(remainder);
        }
        return n == 0;
    }

    public static void Main()
    {
        int sum = 0;
        for (int n = 3; n <= 9999999; n++)
        {
            if (isCurious(n))
                sum += n;
        }
        Console.WriteLine(sum);
    }
}


