from fw_recursion import FW_recursion
from fw_iteritive import floyd
import unittest
import sys

NO_PATH = sys.maxsize

class TestingFWRecursion(unittest.TestCase):
    def test_correctfunction(self):
         graph = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
            ]
         known_min_graph = [
            [0, 7, 12, 8], 
            [9223372036854775807, 0, 5, 7],
            [9223372036854775807, 9223372036854775807, 0, 2], 
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]
            ]
         self.assertEqual(FW_recursion(graph),known_min_graph)

    def test_correctfunction(self):
        


    def test_inputtypes(self):
        graph = [
            [0, "string", NO_PATH],
            [-3, 0, 9],
            [NO_PATH, 1, 0]
        ]
        with self.assertRaises(TypeError):
            FW_recursion(graph)


if __name__ == "__main__":
    unittest.main()