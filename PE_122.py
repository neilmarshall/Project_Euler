#! /usr/bin/env python3.7
"""
The most naive way of computing n15 requires fourteen multiplications:

    n × n × ... × n = n^15

But using a "binary" method you can compute it in six multiplications:

    n × n = n^2
    n^2 × n^2 = n^4
    n^4 × n^4 = n^8
    n^8 × n^4 = n^12
    n^12 × n^2 = n^14
    n^14 × n = n^15

However it is yet possible to compute it in only five multiplications:

    n × n = n^2
    n^2 × n = n^3
    n^3 × n^3 = n^6
    n^6 × n^6 = n^12
    n^12 × n^3 = n^15

We shall define m(k) to be the minimum number of multiplications to compute nk;
for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑m(k).

Solution: 1582
"""
def PE122(limit):
    """
    >>> PE122(200)
    1582
    """
    def get_level(target, level=0, current_paths=[(1, [1])]):
        
        def generate_new_paths(current_paths):
            new_paths = []
            for path in current_paths:
                for existing_sum in path[1]:        
                    new_sums = path[1][:]
                    new_sums.append(path[0] + existing_sum)
                    new_path = (path[0] + existing_sum, new_sums)
                    new_paths.append(new_path)
                    if new_path[0] == target:
                        break
                if new_path[0] == target:
                    break
            return new_paths
            
        if not any(path[0] == target for path in current_paths):
            return get_level(target, level + 1, generate_new_paths(current_paths))
        return level

    return sum(get_level(target) for target in range(1, limit + 1))


if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True) 