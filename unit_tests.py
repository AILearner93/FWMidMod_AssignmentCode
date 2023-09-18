# This code is the unit testing for the Floyd-Warshall algorithm.
# Import FW_recursion function from the fw_recursion.py file in the same directory.
from fw_recursion import FW_recursion
# Import the Python packages that are required for the test to run.
import unittest
import sys

# Define a value for a sufficiently large number that represents infinity.
NO_PATH = sys.maxsize


# Define a class that includes the unit tests for the application.
class TestingFWRecursion(unittest.TestCase):
    # Tests the functionality of the FW_recursion function; correctly computes 
    # the minimum distance in a small input graph.
    def test_correct_function(self):
        # Defining the test graph and the expected result with minimum distances.
        graph = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        known_min_graph = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        # Assert that the output from the FW_recursion function matches 
        # the known minimum distance graph.
        self.assertEqual(FW_recursion(graph), known_min_graph)

    # Tests that a non-square matrix as an input will raise a ValueError.
    def test_non_square_matrix(self):
        graph = [
            [-1, 1, NO_PATH, 1],
            [NO_PATH, 0, -3, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0, 2]  # Additional number here.
        ]
        # Assert that a ValueError is raised due to a non-square matrix input.
        with self.assertRaises(ValueError):
            FW_recursion(graph)

    # Tests that there is a ValueError raised if a negative cycle is present 
    # when computing the minimum distance graph.
    def test_negative_cycles(self):
        graph = [
            [-1, 1, NO_PATH, 1],
            [NO_PATH, 0, -3, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        # Assert that a ValueError is raised in the presence of negative cycles in the graph.
        with self.assertRaises(ValueError):
            FW_recursion(graph)

    # Tests that a TypeError is raised when there is an invalid data type; 
    # the code requires integer or float values.
    def test_input_types(self):
        graph = [
            [0, "string", NO_PATH],
            [-3, 0, 9],
            [NO_PATH, 1, 0]
        ]
        # Assert that a TypeError is raised due to incorrect data type in the graph.
        with self.assertRaises(TypeError):
            FW_recursion(graph)


# Ensure that the tests are run when the script is executed.
if __name__ == "__main__":
    unittest.main()
