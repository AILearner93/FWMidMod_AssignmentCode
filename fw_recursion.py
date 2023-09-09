import sys

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH,1]]
MAX_LENGTH = len(graph[0])

def FW_recursion(distance,int_Node=0):
    """
    A simple implementation of Floyd's algorithm with a recursive funtion#
    this takes in the input of the matrix and also the int node if the into node is present.

    the function will then compute the minimum distance between two of the nodes
    """
    #get the length of the matrix, must be square for it to work.
    distance_length =len(distance)

    if distance_length == int_Node:
        print(distance)
        return distance
    else:
        for start_node in range(distance_length):
            for end_node in range(distance_length):
                distance[start_node][end_node] = min(distance[start_node][end_node],
            distance[start_node][int_Node] + distance[int_Node][end_node] )
        int_Node+=1
        FW_recursion(distance,int_Node)

MinDisGraph=FW_recursion(graph)