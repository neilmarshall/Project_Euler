/*
We shall call a positive integer A an "Alexandrian integer", if there exist
integers p, q, r such that:

    A = p . q . r, and 1 / A = 1 / p + 1 / q + 1 / r

For example, 630 is an Alexandrian integer (p = 5, q = −7, r = −18). In fact,
630 is the 6th Alexandrian integer, the first 6 Alexandrian integers being:

    6, 42, 120, 156, 420 and 630.

Find the 150000th Alexandrian integer.

Note -- The first such integers are:

    [6, 42, 120, 156, 420, 630, 930, 1428, 1806, 2016, 2184, 3192, 4950, 5256,
     8190, 8364, 8970, 10296, 10998, 12210, 17556, 19110, 21114, 23994, 24492,
     28050, 32640, 33306, 34362, 37506, 39270, 44310, 52326, 57684, 57840,
     70686, 74256, 79800, 83076]
    
Solution: 1884161251122450
*/

#include <cmath>

#include <algorithm>
#include <iostream>
#include <vector>


class AlexandrianIntegerGenerator {
    private:
        long limit;
        std::vector<long> A;
        long r;

        // Calculate initial list of values
        void generate_initial_list() {
            while (A.size() < limit) {
                r += 1;
                long p = -(r + 1);
                while (p * p + 2 * p * r - 1 < 0) {
                    double q = (1.0 - p * r) / (p + r);
                    if (floor(q) == q) {
                        A.push_back(p * q * r);
                    }
                    p -= 1;
                }
            }
            std::sort(A.begin(), A.end());
            A.resize(limit);
        }

        // For initial list of values, if subsequent (lower) values can be
        // found then replace components of the initial list greater than
        // the new values
        void optimise_existing_solution() {
            long curMax = A.back();
            while (r * (r + 1) * (r + 2) < curMax) {
                r += 1;
                long p = -(r + 1);
                while (p * p + 2 * p * r - 1 < 0) {
                    double q = (1.0 - p * r) / (p + r);
                    if (floor(q) == q) {
                        if (p * q * r < curMax) {
                            A.back() = p * q * r;
                            std::sort(A.begin(), A.end());
                            curMax = A.back();
                        }
                    }
                    p -= 1;
                }
            }
        }


    public:
        AlexandrianIntegerGenerator(long limit) : limit(limit), r(0) { }

        long solve() {
            generate_initial_list();
            optimise_existing_solution();
            return A.back();
        }
};


int main () {
    AlexandrianIntegerGenerator aig(150000);
    std::cout << aig.solve() << std::endl;
}
