/*
Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing
a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half
of the numbers below one-thousand (525) are bouncy. In fact, the least number
for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we
reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.

Solution: 1587000
*/

#include <iostream>
#include <string>

class Bouncifier {
    private:
        bool increasing (std::string s) {
            if (s.size() == 1) { return true; }
            return s.substr(0, 1) <= s.substr(1, 1) && increasing(s.substr(1));
        }
        bool decreasing (std::string s) {
            if (s.size() == 1) { return true; }
            return s.substr(0, 1) >= s.substr(1, 1) && decreasing(s.substr(1));
        }
    public:
        bool operator () (int n) {
            return !increasing(std::to_string(n)) && ! decreasing(std::to_string(n));
        }
};

int main () {
    Bouncifier bouncifier;
    int bouncy_count = 0;
    int n = 1;
    while (bouncy_count / static_cast<double>(n) < 0.99) {
        n += 1;
        if (bouncifier(n)) { bouncy_count += 1; }
    }
    std::cout << n << std::endl;
}
