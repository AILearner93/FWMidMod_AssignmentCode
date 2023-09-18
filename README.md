# Floyd-Warshall Recursive Algorithm _(FWMidMod_AssignmentCode)_

Source code for the Floyd-Warshall algorithm, developed for the Mid Module Assignment including Unit and Performance tests.

The script implements the Floyd-Warshall algorithm, a dynamic programming solution to find the shortest paths between all pairs of vertices in a weighted directed graph. The algorithm is implemented through a recursive function that iteratively updates a distance matrix until the shortest paths between all pairs of nodes are found or until it detects a negative cycle in the graph. 

## Installing

  To install this project, follow the steps below:

1. **Download the latest zip file from this repository**
2. **Unzip the file into a desired location**

  Alternatively using git to clone the repository.

  ```sh
  git clone https://github.com/AILearner93/FWMidMod_AssignmentCode
  ```

## Execution

Before you begin execution make sure you have python 3.X.X installed on your system.

  ```sh
  python3 --version
  ```


1. **Using your preferred command line interface (CLI) navigate to the directory where you unzipped or cloned the files from this repository.**
2. **Install all the required packages for this application.**

  ```sh
  pip install -r requirements.txt
  ```

3. **Run the fw_recursion script**

  ```sh
  python fw_recursion.py
  ```

## Tests:

The section below demonstrates the types of tests that are incorporated into the Unit Testing.

#### Valid Input Test:
    Input : a valid square matrix representing a graph.

    Expected Output : an updated matrix with the shortest path distances between all nodes.


#### Non-Square Matrix Test:
    Input : a non-square matrix.

    Expected Output: a ValueError with an appropriate error message.

#### Invalid Element Type Test:
    Input : a matrix containing non-numeric values.

    Expected Output : a TypeError with an appropriate error message.

#### Negative Cycle Test:
    Input : a matrix representing a graph with a negative cycle.

    Expected Output a ValueError with an appropriate error message.

