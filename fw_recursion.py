import sys

NO_PATH = sys.maxsize

def FW_recursion(distance,int_Node=0):
    """
    A simple implementation of Floyd's algorithm with a recursive funtion#
    this takes in the input of the graph array and also the int node if the into node is present.

    the function will then compute the minimum distance between two of the nodes

    It also carries out check for if the graph is square and if incorrect datatypes are in the graph
    """
    distance_length =len(distance)

    for row in distance:
        if len(distance) != len(row):
            raise ValueError("Matrix is not square")

    for row in distance:
        if not all(isinstance(elem, (int,float)) for elem in row) :
            raise TypeError("The elements in this graph need to be of type int or floats")
    




    #get the length of the matrix, must be square for it to work
    if distance_length == int_Node:
        for i in range(distance_length):
            if distance [i][i] < 0:
                raise ValueError("This graph containes a negative cycle")
        print (distance)
        return distance
    else:
        for i in range(distance_length):
            for j in range(distance_length):
                distance[i][j] = min(distance[i][j],
            distance[i][int_Node] + distance[int_Node][j] )
        int_Node+=1
        return FW_recursion(distance,int_Node)

initial_graph = [
    [0, 1, 1],
    [NO_PATH, 0, 2],
    [3, NO_PATH, 0]
]

FW_recursion(initial_graph)

