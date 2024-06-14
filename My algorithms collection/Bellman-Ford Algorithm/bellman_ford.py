class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def bellman_ford(edges, V, src):
    distance = [float('inf')] * V
    distance[src] = 0

    for _ in range(V - 1):
        for edge in edges:
            if distance[edge.u] + edge.w < distance[edge.v]:
                distance[edge.v] = distance[edge.u] + edge.w

    for edge in edges:
        if distance[edge.u] + edge.w < distance[edge.v]:
            print("Graph contains negative weight cycle")
            return

    print("Vertex Distance from Source")
    for i in range(V):
        print(f"{i}\t{distance[i]}")


edges = [Edge(0, 1, -1), Edge(0, 2, 4), Edge(1, 2, 3), Edge(1, 3, 2), Edge(1, 4, 2), Edge(3, 2, 5), Edge(3, 1, 1), Edge(4, 3, -3)]
V = 5
src = 0
bellman_ford(edges, V, src)
