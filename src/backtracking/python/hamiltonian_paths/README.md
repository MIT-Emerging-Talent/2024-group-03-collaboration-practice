# Hamiltonian paths 

This package implements searching all possible Hamiltonian paths in a graph using a depth-first search (DFS) algorithm.

## Package Structure

The package consists of the following Python files: 
hamiltonian_paths.py: Contains the main logic for DFS algorithm. Also implements Graph class. 
test_hamiltonian_paths.py: Contains the unit tests for the hamiltonian_paths.py functions using sample data.

## Files Descriptions

### Graph Class
The Graph class is a representation of an undirected graph.
num_nodes stores the number of nodes in the graph, initialized to 0.
edges is a dictionary where each node is a key, and the corresponding value is a list of nodes adjacent to it.

## Test File

test_hamiltonian_paths.py contains the test cases for the classes and methods in hamiltonian_paths.py. The tests use sample data to verify that the implemented methods correctly execute DFS algorithm.