// The positive integers, x, y, and z, are consecutive terms of an arithmetic
// progression. Given that n is a positive integer, the equation, x^2 − y^2 − z^2 = n,
// has exactly one solution when n = 20:
//
// 13^2 − 10^2 − 7^2 = 20
//
// In fact there are twenty-five values of n below one hundred for which the
// equation has a unique solution.
//
// How many values of n less than fifty million have exactly one solution?
//
// Solution: 2544559

#include <cmath>

#include <iostream>
#include <map>

int main()
{
	int limit = 100, e = 1;
	//int limit = 50000000, e = 1;
	std::map<int, int> solution_counter;
	while (4 * e - 1 <= limit) {
		if (e % 1000 == 0) std::cout << e << '\n';
		int x_min = 4 * e * e - limit < 0 ? 1 : int(e + sqrt(4 * e * e - limit));
		for (int x = x_min; x < 3 * e; x++) {
			int n = (e + x) * (3 * e - x);
			if (n <= limit) {
				solution_counter[n] = +1;
			}
		}
		e += 1;
	}

	int total = 0;
	for (auto solution : solution_counter) {
		std::cout << solution.first << ' ' << solution.second << '\n';
		if (solution.second == 1)
			total += 1;// solution.first;
	}
	std::cout << total << std::endl;
}
