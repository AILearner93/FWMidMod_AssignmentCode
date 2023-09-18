"""
This script performs unit testing for the Floyd-Warshall algorithm using 
both recursive and iterative methods. It leverages NumPy for matrix 
operations and pandas for result presentation.
"""

from fw_recursion import FW_recursion
from fw_iteritive import floyd
import timeit
import pandas as pd
import numpy as np

# Define a value for a sufficiently large number that represents infinity. 
NO_PATH = 999999


def random_matrix(size):
    """Generate a random distance matrix using NumPy.
    
    This initializes the matrix with random numbers between 0 and 100. 
    The function also ensures that the diagonals are filled with 0, as required for the distance matrix.
    """
    matrix = np.random.randint(1, 100, (size, size))
    # Randomly assign NO_PATH at a probability of 50%
    matrix[np.random.rand(size, size) < 0.5] = NO_PATH
    # Fill the diagonal of the matrix with zeros
    np.fill_diagonal(matrix, 0)
    return matrix.tolist()


def wrapper(func, *args, **kwargs):
    """Define a wrapper function required for the timeit performance testing."""
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def main():
    """Main function that conducts performance tests based on the nodes in the nodes list.
    
    To test for performance, the nodes list is iterated through to generate random matrices. 
    These matrices are tested through both the recursive and iterative functions 100 times. 
    The results are tabulated in a data frame and output to the CLI.
    """
    nodeslist = [5, 10, 50, 100]

    results = []  # Create a list to be filled with the below values
    for nodes in nodeslist:
        matrix = random_matrix(nodes)

        recursive_wrapped = wrapper(FW_recursion, matrix)
        iterative_wrapped = wrapper(floyd, matrix)

        recursive_time = timeit.timeit(recursive_wrapped, number=100)
        iterative_time = timeit.timeit(iterative_wrapped, number=100)
        results.append([f"{nodes}x{nodes}", recursive_time, iterative_time])

    result_df = pd.DataFrame(results, columns=["Matrix Size", "Recursive Time (s)", "Iterative Time (s)"])

    print(result_df.to_string(index=False))


# Ensure that the performance tests are run when the script is executed.
if __name__ == "__main__":
    main()