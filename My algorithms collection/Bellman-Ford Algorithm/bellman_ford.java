import java.util.*;

class Edge {
    int u, v, w;
    Edge(int u, int v, int w) {
        this.u = u;
        this.v = v;
        this.w = w;
    }
}

public class BellmanFord {
    void bellmanFord(List<Edge> edges, int V, int src) {
        int[] distance = new int[V];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[src] = 0;

        for (int i = 1; i < V; ++i) {
            for (Edge edge : edges) {
                if (distance[edge.u] != Integer.MAX_VALUE && distance[edge.u] + edge.w < distance[edge.v]) {
                    distance[edge.v] = distance[edge.u] + edge.w;
                }
            }
        }

        for (Edge edge : edges) {
            if (distance[edge.u] != Integer.MAX_VALUE && distance[edge.u] + edge.w < distance[edge.v]) {
                System.out.println("Graph contains negative weight cycle");
                return;
            }
        }

        System.out.println("Vertex Distance from Source");
        for (int i = 0; i < V; ++i) {
            System.out.println(i + "\t" + distance[i]);
        }
    }

    public static void main(String[] args) {
        List<Edge> edges = Arrays.asList(
            new Edge(0, 1, -1), new Edge(0, 2, 4),
            new Edge(1, 2, 3), new Edge(1, 3, 2),
            new Edge(1, 4, 2), new Edge(3, 2, 5),
            new Edge(3, 1, 1), new Edge(4, 3, -3)
        );
        int V = 5;
        int src = 0;
        new BellmanFord().bellmanFord(edges, V, src);
    }
}
