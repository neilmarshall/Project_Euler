#! /usr/local/bin/python3.7
"""
Using network.txt (right click and 'Save Link/Target As...'), a 6K text file
containing a network with forty vertices, and given in matrix form, find the
maximum saving which can be achieved by removing redundant edges whilst
ensuring that the network remains connected.

Solution: 259679
"""
from itertools import product

def load_network(filename):
    network = []
    with open(filename, 'r') as f_obj:
        for line in f_obj:
            network.append(list(map(int, line.replace('\n', '').replace('-', '0').split(','))))
    return network


def get_weights(network, connected_nodes, neighbours):
    weights = [network[connected_node][neighbour]
               for connected_node in connected_nodes
               for neighbour in neighbours
               if network[connected_node][neighbour] != 0]    
    return weights


def PE_107():
    """
    >>> PE_107()
    259679
    """
    network = load_network('p107_network.txt')

    unminimised_weight = sum(sum(line) for line in network) // 2
    current_weight = minimised_weight = min(min(filter(lambda n: n != 0, line)) for line in network)

    connected_nodes, unconnected_nodes = [], list(range(len(network)))
    for i, j in product(range(len(network)), repeat=2):
        if network[i][j] == current_weight:
            connected_nodes.append(i)
            unconnected_nodes.remove(i)

    neighbours = []
    while unconnected_nodes or neighbours:
        for connected_node in connected_nodes:
            for unconnected_node in unconnected_nodes:
                if network[connected_node][unconnected_node] != 0:
                    neighbours.append(unconnected_node)
                    unconnected_nodes.remove(unconnected_node)
        current_weight = min(get_weights(network, connected_nodes, neighbours))
        minimised_weight += current_weight
        for i, j in product(range(len(network)), repeat=2):
            if ((network[i][j] == current_weight) and (i not in connected_nodes) and (j in connected_nodes)):
                connected_nodes.append(i)
                neighbours.remove(i)

    return unminimised_weight - minimised_weight


if __name__ == '__main__':
    import doctest; doctest.testmod()
