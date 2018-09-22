#include "square_checker.h"

bool square_checker::operator()(long n) {
    bool val = false;
    if (checked_numbers.find(n) != checked_numbers.end()) {
        val = checked_numbers[n];
    } else {
        for (long i = 1; i * i <= n; ++i) {
            if (i * i == n) val = true;
        }
        checked_numbers.insert(std::pair<long, bool>(n, val));
    }
    return val;
}

