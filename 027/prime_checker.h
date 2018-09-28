#ifndef PRIME_CHECKER_H
#define PRIME_CHECKER_H

#include <cmath>

#include <map>

/*
    A class that checks primality of numbers, remembering numbers
    that have already been checked
*/
class Prime_Checker {
    private:
        std::map<int, bool> known_values;

    public:
        bool operator() (int n) {

            if ( n < 0) return false;  // negative numbers are not considered prime

            auto known_value = known_values.find(n);

            // if value already known
            if (known_value != known_values.end())
                return known_value->second;

            // if value not already known
            for (int p = 2; p <= static_cast<int>(sqrt(n)); p++) {
                if (n % p == 0) {
                    known_values[n] = false;
                    return false;
                }
            }
            known_values[n] = true;
            return true;
        }
};

#endif /* PRIME_CHECKER_H */
