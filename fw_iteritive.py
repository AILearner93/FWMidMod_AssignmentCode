#course coding notes for FW, commented by T.An

import sys
import itertools

NO_PATH = sys.maxsize
initialise_graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]


def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    MAX_LENGTH = len(distance[0])

    for intermediate, start_node,end_node\
    in itertools.product\
    (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        #return all possible paths and find the minimum
        #graph[rownumber][columnnumber] = returns value that is in position of list graph
        #below code updates the value with the smallest value out of current value in that position versus that path with the intermediate nodes
        distance[start_node][end_node] = min(distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node] )
    #Any value that have sys.maxsize has no path
    print (distance)
    return distance
floyd(initialise_graph)