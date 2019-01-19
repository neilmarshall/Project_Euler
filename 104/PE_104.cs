// The Fibonacci sequence is defined by the recurrence relation:
//     F(n) = F(n − 1) + F(n − 2), where F(1) = 1 and F(2) = 1.
//
// It turns out that F(541), which contains 113 digits, is the first Fibonacci number
// for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9,
// but not necessarily in order). And F(2749), which contains 575 digits, is the first
// Fibonacci number for which the first nine digits are 1-9 pandigital.
//
// Given that F(k) is the first Fibonacci number for which the first nine digits AND
// the last nine digits are 1-9 pandigital, find k.
//
// Solution: 329468

using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace PE_104
{
    class FibonacciGenerator : IEnumerable<List<int>>
    {
        private List<int> n0;
        private List<int> n1;

        public FibonacciGenerator()
        {
            n0 = new List<int> { 0 };
            n1 = new List<int> { 1 };
        }

        private void Increment()
        {
            List<int> temp = new List<int>(n1);
            n1 = AddArrays();
            n0 = temp;
        }

        private List<int> AddArrays()
        {
            List<int> temp = new List<int>();
            while (n0.Count < n1.Count) { n0.Add(0); }
            int carry = 0;
            for (int i = 0; i < n1.Count; i++)
            {
                int element = n0[i] + n1[i] + carry;
                temp.Add(element % 10);
                carry = element / 10;
            }
            if (carry != 0) { temp.Add(carry); }
            return temp;
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
        public IEnumerator<List<int>> GetEnumerator()
        {
            while (true)
            {
                yield return n1;
                Increment();
            }
        }
    }

    static class IsPandigital
    {
        private static bool IsLeadingPandigital(List<int> s)
        {
            if (s.Count < 9) { return false; }
            var leadingChars = s.TakeLast(9).OrderBy(c => c).ToList();
            for (int i = 0; i < 9; i++)
                if (leadingChars[i] != i + 1) { return false; }
            return true;
        }

        private static bool IsTrailingPandigital(List<int> s)
        {
            if (s.Count < 9) { return false; }
            var trailingChars = s.Take(9).OrderBy(c => c).ToList();
            for (int i = 0; i < 9; i++)
                if (trailingChars[i] != i + 1) { return false; }
            return true;
        }

        public static bool IsDoublyPandigital(List<int> s)
        {
            return IsLeadingPandigital(s) && IsTrailingPandigital(s);
        }
    }


    class Program
    {
        static void Main(string[] args)
        {
            FibonacciGenerator fibGen = new FibonacciGenerator();
            int n = 0;
            foreach (var fib in fibGen)
            {
                n += 1;
                //if (n % 1000 == 0) { Console.WriteLine(n); }
                if (IsPandigital.IsDoublyPandigital(fib))
                {
                    Console.WriteLine(n);
                    break;
                }
            }
        }
    }
}
