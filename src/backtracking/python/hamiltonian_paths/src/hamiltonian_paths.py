# Define a class to represent an undirected graph
class Graph:
    def __init__(self): # Initialize the number of nodes and the adjacency dictionary
        self.num_nodes = 0
        self.edges = {}

    # Method to add an undirected edge between nodes l and r
    def add_edge(self, l, r):
        if l not in self.edges:
            self.edges[l] = []

        if r not in self.edges:
            self.edges[r] = []
        # Add edges to the adjacency lists
        self.edges[l].append(r)
        self.edges[r].append(l)
        if len(self.edges) > self.num_nodes:
            self.num_nodes = len(self.edges)


def find_hamiltonian_paths(G):
    """ Function to find all Hamiltonian paths in an undirected graph
        Nested function for depth-first search to explore Hamiltonian paths
        If all vertices are visited, a Hamiltonian path exists"""

    def dfs(G, r, visited, path):
        if len(path) == len(G.edges):
            paths.append(path.copy())
            return

        # Check if node `r` has any outgoing edges
        if r not in G.edges:
            return

        # Check if every edge starting from vertex `r` leads to a solution or not
        for w in G.edges[r]:
            """Process only unvisited vertices as the Hamiltonian
                path visit each vertex exactly once"""
            if not visited[w]:
                visited[w] = True
                path.append(w)

                #Recursively check if adding node `w` to the path leads to the solution or not
                dfs(G, w, visited, path)

                # Backtrack
                visited[w] = False
                path.pop()

    #Iterate through every node in the graph and start the search from each node
    paths = []
    for start in range(len(G.edges)):
        # Add starting node to the path
        path = [start]
        # Mark starting node as visited
        visited = [False] * len(G.edges)
        visited[start] = True
        # Call the depth-first search function
        dfs(G, start, visited, path)
    return paths
