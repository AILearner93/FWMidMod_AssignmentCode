import sys

NO_PATH = sys.maxsize


def fw_recursion(distance, int_node=0):
    """
    A simple implementation of Floyd's algorithm using a recursive function.

    This function computes the minimum distance between all pairs of nodes in a graph represented by a square matrix.
    
    Parameters:
    distance (list of list of int/float): The adjacency matrix of the graph where `sys.maxsize` represents no path between nodes.
    int_node (int, optional): The intermediate node used in the recursive calculation. Defaults to 0.
    
    Returns:
    list of list of int/float: The adjacency matrix with the minimum distances between all pairs of nodes.
    
    Raises:
    ValueError: If the input matrix is not square or contains a negative cycle.
    TypeError: If the matrix contains elements that are not int or float.
    """
    distance_length = len(distance)

    for row in distance:
        if len(distance) != len(row):
            raise ValueError("The input is not a square matrix, please check input.")
    
    for row in distance:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("The elements in this graph need to be of type int or float, please check input.")

    # Base case for the algorithm: when the intermediate node counter matches the number of nodes in the graph
    if distance_length == int_node:
        for i in range(distance_length):
            if distance[i][i] < 0:
                raise ValueError("This graph contains a negative cycle; this algorithm is not suitable.")
        return distance

    # Recursive case for the algorithm: update distances using the current intermediate node and increment the node counter
    else:
        for i in range(distance_length):
            for j in range(distance_length):
                distance[i][j] = min(distance[i][j], distance[i][int_node] + distance[int_node][j])
        int_node += 1
        return fw_recursion(distance, int_node)


# Example usage with a 3x3 initial graph
initial_graph = [
    [0, 1, 1],
    [NO_PATH, 0, 2],
    [3, NO_PATH, 0]
]

resulting_graph = fw_recursion(initial_graph)
print(resulting_graph)
