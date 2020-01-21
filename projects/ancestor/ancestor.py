from graph import Graph
sequence = []
def earliest_ancestor(ancestors, starting_node):
    for pairs in ancestors:
        if pairs[1] == starting_node:
            sequence.append(pairs[1])
            print(sequence)
            earliest_ancestor(ancestors, pairs[0])
        
    return sequence

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))
