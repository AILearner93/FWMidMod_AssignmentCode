from ..fw_recursion import FW_recursion
import unittest

class TestingFWRecursion(unittest.TestCase):
    def test_smallmatrix(self):
        matrix = [
            [0, 3, float(inf)],
            [10, 0, 9],
            [float(inf), 1, 0]
        ]
        with self.assertRaises(ValueError):
            FW_recursion(matrix)


if __name__ == "__main__":
    unittest.main()