def kruskal(graph):
    """
    Implement Kruskal's algorithm to find the minimum spanning tree of a graph.

    Parameters:
    graph (Graph): The graph on which to apply Kruskal's algorithm.

    Returns:
    int: The total weight of the minimum spanning tree.
    """
    vertex_rank = dict()
    parent = dict()

    parent = {}
    vertex_rank = {}

    def find(vertex):
        if vertex != parent[vertex]:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(root1, root2):
        if vertex_rank[root1] > vertex_rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if vertex_rank[root1] == vertex_rank[root2]:
                vertex_rank[root2] += 1

    for vertex in graph.vertices():
        parent[vertex] = vertex
        vertex_rank[vertex] = 0

    mst_weight = 0
    for edge in sorted(graph.edges(), key=lambda e: e.distance):
        root1, root2 = find(edge.source), find(edge.destination)
        if root1 != root2:
            mst_weight += edge.distance
            union(root1, root2)

    return mst_weight
