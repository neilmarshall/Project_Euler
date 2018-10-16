/*
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains
eighteen rectangles.

Although there exists no rectangular grid that contains exactly two million
rectangles, find the area of the grid with the nearest solution.

Solution: 2772
*/

#include <iostream>
#include <tuple>

int count_subgrids(const int& width, const int& height) {
    int subgrid_count = 0;
    for (int w = 1; w <= width; w++) {
        for (int h = 1; h <= height; h++) {
            subgrid_count += (1 + width - w) * (1 + height - h);
        }
    }
    return subgrid_count;
}

std::tuple<int, int> dimensions_of_grid_with_at_most_n_subgrids (const int& target) {
    
    int subgridcount, width = 2, height = 2, margin = target;
    std::tuple<int, int> result;
	
    while (count_subgrids(2, height) <= target) {
        width = 2;
        height += 1;
        while (count_subgrids(width, height) <= target) {
            width += 1;	
            subgridcount = count_subgrids(width, height);
            if (abs(target - subgridcount) < margin) {
                margin = abs(target - subgridcount);
                result = std::make_tuple(width, height);
            }
        }
    }

    return result;
}

int main() {

    const int target = 2000000;

    int width, height;
    std::tie(width, height) = dimensions_of_grid_with_at_most_n_subgrids(target);

    std::cout << "area: " << width * height << std::endl;
}
