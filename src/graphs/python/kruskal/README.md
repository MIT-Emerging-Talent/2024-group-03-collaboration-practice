# Kruskal's Algorithm

This package implements Kruskal's Algorithm using Python. Kruskal's Algorithm is a famous greedy algorithm used to solve the minimum spanning tree for a connected, undirected and weighted graph.

## Package Structure

The package consists of the following Python files:
kruskal.py: Contains the main logic for Kruskal's algorithm. Also implements the Vertex, Edge, and Graph classes.
test_kruskal.py: Contains the unit tests for the kruskal.py functions using sample data.

## Files Descriptions

**Vertex Class**

A Vertex is a single node in the graph and has been implemented in this file. It expects an identifier as an attribute for each Vertex object.

```python
class Vertex:
    def __init__(self, value):
        self.value = value
    ...
```

**Edge Class**

The Edge class models a pathway between two vertices or nodes. An Edge is defined by two properties: the nodes or vertices it connects together, and the weight or cost of traversal.
```python
class Edge:
    def __init__(self, source, destination, distance):
        self.source = source
        self.destination = destination
        self.distance = distance
    ...
```

**Graph Class**

A Graph is basically a set of vertices and edges. It contains a list of vertices and each vertex has a list of neighbors(edges). The Graph class is the main interface for using this library.
```python
class Graph:
    def __init__(self):
        self._adj_dict = dict()
    ...
```

**Test File**

test_kruskal.py contains the test cases for the classes and methods in kruskal.py. The tests use sample data to verify that the implemented methods correctly execute Kruskal's Algorithm.

