/**
 * Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for
 * any two non-empty disjoint subsets, B and C, the following properties are true:
 * 
 *     1. S(B) ≠ S(C); that is, sums of subsets cannot be equal.
 *     2. If B contains more elements than C then S(B) > S(C).
 *
 * For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84,
 * whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair
 * combinations and S(A) = 1286.
 * 
 * Using sets.txt, a 4K text file with one-hundred sets containing seven to twelve elements (the two examples
 * given above are the first two sets in the file), identify all the special sum sets, A1, A2, ..., Ak, and
 * find the value of S(A1) + S(A2) + ... + S(Ak).  NOTE: This problem is related to Problem 103 and Problem 106.
 * 
 * SOLUTION: 73702
**/

var result = System.IO.File.ReadAllLines("p105_sets.txt")
    .Select(line => line.Split(",").Select(int.Parse).OrderBy(n => n).ToArray())
    .Where(IsSpecialSumSet)
    .Sum(s => s.Sum());

Console.WriteLine(result);

static bool IsSpecialSumSet(int[] values)
{
    if (Enumerable.Range(1, values.Length).Any(p => values.Skip(p).Sum() > values.Take(values.Length - p + 1).Sum()))
        return false;

    List<int> sums = new() { values[0] };
    foreach (var i in Enumerable.Range(1, values.Length - 1))
    {
        sums.AddRange(Enumerable.Range(0, sums.Count).Select((e, j) => values[i] + sums[j]));
        sums.Add(values[i]);
    }
    sums.Sort();

    return sums.Zip(sums.Skip(1), (a, b) => a != b).All(e => e);
}
