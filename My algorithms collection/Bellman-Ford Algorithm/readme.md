# Bellman-Ford Algorithm

## Introduction

The Bellman-Ford algorithm computes the shortest paths from a single source vertex to all other vertices in a weighted graph. It is capable of handling graphs with negative weight edges and can detect negative weight cycles.

## How It Works

1. Initialize the distance to the source vertex to 0 and the distance to all other vertices to infinity.
2. Relax all edges |V| - 1 times, where |V| is the number of vertices in the graph.
3. Check for negative weight cycles by verifying if further relaxation is possible.

### Time Complexity

- **Worst-case time complexity**: quadratic: O(V * E), where V is the number of vertices and E is the number of edges. 

## Pseudocode

```plaintext
function BellmanFord(graph, V, E, src):
    distance[] <- Initialize distances from src to all other vertices as INFINITE
    distance[src] <- 0

    for i from 1 to V-1:
        for each edge (u, v, weight) in E:
            if distance[u] + weight < distance[v]:
                distance[v] <- distance[u] + weight

    for each edge (u, v, weight) in E:
        if distance[u] + weight < distance[v]:
            print "Graph contains negative weight cycle"
            return

    print "Vertex Distance from Source"
    for i from 0 to V-1:
        print i, distance[i]
