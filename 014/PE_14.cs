/*
   The following iterative sequence is defined for the set of positive longegers:

   n → n / 2 (n is even)
   n → 3 * n + 1 (n is odd)

   Using the rule above and starting with 13, we generate the following sequence:

   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

   It can be seen that this sequence (starting at 13 and finishing at 1) contains
   10 terms. Although it has not been proved yet (Collatz Problem), it is thought
   that all starting numbers finish at 1.

   Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
 */

using System;

class Program
{
    private static long calculate_sequence_length(long n)
    {
        long count = 1;

        while (n != 1)
        {
            if (n % 2 ==0)
            {
                n /= 2;
            }
            else
            {
                n = 3 * n + 1;
            }
            count += 1;
        }

        return count;
    }

    public static void Main(string[] argv)
    {
        long max_chain_length = 0, solution = 0;
        for (long n = 1; n < 1000000; n++)
        {
            long chain_length = calculate_sequence_length(n);
            if (chain_length > max_chain_length)
            {
                solution = n;
                max_chain_length = chain_length;
            }
        }
        Console.WriteLine("Solution: {0}", solution);
    }
}

