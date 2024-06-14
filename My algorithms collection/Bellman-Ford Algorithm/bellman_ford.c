#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

struct Edge {
    int u, v, w;
};

void bellmanFord(struct Edge edges[], int V, int E, int src) {
    int distance[V];
    for (int i = 0; i < V; i++)
        distance[i] = INT_MAX;
    distance[src] = 0;

    for (int i = 1; i <= V - 1; i++) {
        for (int j = 0; j < E; j++) {
            int u = edges[j].u;
            int v = edges[j].v;
            int w = edges[j].w;
            if (distance[u] != INT_MAX && distance[u] + w < distance[v]) {
                distance[v] = distance[u] + w;
            }
        }
    }

    for (int i = 0; i < E; i++) {
        int u = edges[i].u;
        int v = edges[i].v;
        int w = edges[i].w;
        if (distance[u] != INT_MAX && distance[u] + w < distance[v]) {
            printf("Graph contains negative weight cycle\n");
            return;
        }
    }

    printf("Vertex Distance from Source\n");
    for (int i = 0; i < V; i++) {
        printf("%d\t%d\n", i, distance[i]);
    }
}


int main() {
    struct Edge edges[] = {
        {0, 1, -1}, {0, 2, 4},
        {1, 2, 3}, {1, 3, 2},
        {1, 4, 2}, {3, 2, 5},
        {3, 1, 1}, {4, 3, -3}
    };
    int V = 5;
    int E = sizeof(edges) / sizeof(edges[0]);
    int src = 0;
    bellmanFord(edges, V, E, src);
    return 0;
}
