# Floyd-Warshall Recursive Algorithm _(FWMidMod_AssignmentCode)_

Source code for the Floyd-Warshall algorithm, developed for the Mid Module Assignment including Unit and Performance tests.

The script implements the Floyd-Warshall algorithm, a dynamic programming solution to find the shortest paths between all pairs of vertices in a weighted directed graph. The algorithm is implemented through a recursive function that iteratively updates a distance matrix until the shortest paths between all pairs of nodes are found or until it detects a negative cycle in the graph. 

# FW Recursion Script

This script implements the Floyd-Warshall algorithm using recursion to find the shortest paths in a weighted graph with positive or negative edge weights (but no negative cycles).

## Installing

  To install this project, follow the steps below:

1. **Download the latest zip file from this repository**
2. **Unzip the file into a desired location""

  alternatively using git to clone the repositery.

  ```sh
  git clone https://github.com/AILearner93/FWMidMod_AssignmentCode
  ```

### Excecution

###Tests:
  To ensure that the script works correctly and handles edge cases well, you can create a series of tests including but not limited to the following:

Valid Input Test:

Input: a valid square matrix representing a graph.
Expected Output: an updated matrix with the shortest path distances between all nodes.
Non-Square Matrix Test:

Input: a non-square matrix.
Expected Output: a ValueError with an appropriate error message.
Invalid Element Type Test:

Input: a matrix containing non-numeric values.
Expected Output: a TypeError with an appropriate error message.
Negative Cycle Test:

Input: a matrix representing a graph with a negative cycle.
Expected Output: a ValueError with an appropriate error message.
Large Graph Test:

Input: a large graph with many nodes and edges.
Expected Output: the function should return the correct distance matrix within a reasonable time.

