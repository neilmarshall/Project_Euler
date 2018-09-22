#include "square_checker.h"

#include <iostream>

int main(int argc, char* argv[]) {

    /*
    Expected answers:
        m = 1000    --> 72
        m = 2000    --> 100
        m = 10000   --> 210
        m = 100000  --> 616
        m = 1000000 --> 1818
    */

    long limit = atol(argv[1]);
    long l = 0;
    long solutionCount = 0;
    long pathLength = 0;
 
    square_checker square_check;

    while (solutionCount < limit) {
        l += 1;
        for (long w = 1; w < l + 1; w += 1) {
	    for (long h = 1; h < w + 1; h += 1) {
		pathLength = l * l + (w + h) * (w + h);
                if (square_check(pathLength)) solutionCount += 1;
            }
        }
    }
 
    std::cout << "M = " << l << std::endl;

    return 0;
}
