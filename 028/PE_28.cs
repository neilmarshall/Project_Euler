using System;

class Program
{
    /// Returns sum of diagonals of a number-spiral of size n x n
    /// Test cases:
    ///     >>> number_spiral_diagonal_sum(1) = 1
    ///     >>> number_spiral_diagonal_sum(3) = 25
    ///     >>> number_spiral_diagonal_sum(5) = 101
    ///     >>> number_spiral_diagonal_sum(7) = 261
    ///     >>> number_spiral_diagonal_sum(1001) = 669171001
    static long number_spiral_diagonal_sum(long n) {
    
        // program only works for odd integer input
        if (n % 2 != 1) {
            Console.Error.WriteLine("n must be an odd integer");
            Environment.Exit(1);
        }
    
        long s = 1;
        for (long t = 3; t <= n; t += 2) {
            s += 4 * t * t - 6 * (t - 1);
        }
        return s;
    }

    static void Main()
    {
        long[] test_values = {1, 3, 5, 7, 1001, 2};
        foreach (long test_value in test_values) {
            Console.WriteLine(test_value + ": " + number_spiral_diagonal_sum(test_value));
        }
    }
}
