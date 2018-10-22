#! /usr/bin/env python3.6
"""
A row measuring seven units in length has red blocks with a minimum length of
three units placed on it, such that any two red blocks (which are allowed to be
different lengths) are separated by at least one black square. There are exactly
seventeen ways of doing this.

How many ways can a row measuring fifty units in length be filled?

Solution: 16475640049
"""
def extend_block_counter(block_counter, min_subblock_length):
    total_block_length = len(block_counter)
    triangle = lambda x: x * (x + 1) // 2
    new_block = [1, triangle(total_block_length - min_subblock_length + 1)]
    block_count = (total_block_length + 1) // (min_subblock_length + 1) + 1
    j = 2
    while len(new_block) < block_count:
        if block_count == (total_block_length + 1) / (min_subblock_length + 1) + 1 and \
           len(new_block) == block_count - 1:
            new_block.append(1)
        else:
            new_element = block_counter[total_block_length - 1][j] + \
                sum(block_counter[i][j - 1]
                    for i in range(1, total_block_length - min_subblock_length)
                    if len(block_counter[i]) > j - 1)
            j += 1
            new_block.append(new_element)
    block_counter.append(new_block)


def count_ways_of_splitting_block(total_block_length, min_subblock_length):
    """
    >>> count_ways_of_splitting_block(50, 3)
    16475640049
    """
    block_counter = [[] for _ in range(min_subblock_length)] + [[1, 1]]
    while len(block_counter) <= total_block_length:
        extend_block_counter(block_counter, min_subblock_length)
    return sum(block_counter[total_block_length])

if __name__ == '__main__':
    import doctest; doctest.testmod(verbose=True)
