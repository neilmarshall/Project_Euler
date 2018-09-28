/*
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:

    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97

How many circular primes are there below one million?
*/

using System;

class Program
{
    /* Return primality of n */
    private static bool isPrime(int n)
    {
        for (int p = 2; p <= (int)Math.Sqrt(n); p++)
        {
            if (n % p == 0) return false;
        }
        return true;
    }

    /* Return circular primality of n */
    private static bool isCircularPrime(int n)
    {
        string s = n.ToString();
        for (int i = 0; i < s.Length; i++)
        {
            int p;
            Int32.TryParse(s, out p);
            if (!isPrime(p)) return false;
            s = s.Substring(1) + s.Substring(0, 1);    
        }
        return true;
    }

    /* Return number of circular primes less than n */
    public static void Main()
    {

        int circular_prime_count = 0;

        for (int n = 2; n <= 1000000; n++)
        {
            if (isCircularPrime(n)) circular_prime_count += 1;
        }

        Console.WriteLine(circular_prime_count);
    }
}
