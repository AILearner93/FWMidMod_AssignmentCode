import sys
import itertools

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
    #change this to find from graph but currently it works for code
    distancenumber = 4

    if distancenumber == int_Node:
        return distance
    else:
        for start_node in range(distancenumber):
            for end_node in range(distancenumber):
                distance[start_node][end_node] = min(distance[start_node][end_node],
            distance[start_node][int_Node] + distance[int_Node][end_node] )
        int_Node+=1
        FW_recursion(distance,int_Node)

FW_recursion(graph)