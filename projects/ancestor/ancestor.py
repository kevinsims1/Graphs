from graph import Graph
from util import Queue

# Write a function that, given the dataset and the ID of an individual in the dataset, 
# returns their earliest known ancestor – the one at the farthest distance from the input 
# individual. If there is more than one ancestor tied for "earliest", return the one with the 
# lowest numeric ID. If the input individual has no parents, the function should return -1.

def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pairs in ancestors:
        graph.add_vertex(pairs[0])
        graph.add_vertex(pairs[1])
        # print('parent', pairs[0])
        # print('child', pairs[1])
        graph.add_edge(pairs[1], pairs[0])
        # print('vertices', graph.vertices)

    # Do a BFS(Storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        # If the path is longer or equal and the value is smaller, or if the path is longer
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# earliest_ancestor(test_ancestors, 1)

#Notes 
# if pair[child] in vertices
# add parent as 
