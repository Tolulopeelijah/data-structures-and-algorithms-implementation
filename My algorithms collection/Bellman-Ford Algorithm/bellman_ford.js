class Edge {
    constructor(u, v, w) {
        this.u = u;
        this.v = v;
        this.w = w;
    }
}

function bellmanFord(edges, V, src) {
    let distance = Array(V).fill(Infinity);
    distance[src] = 0;

    for (let i = 1; i < V; ++i) {
        for (const edge of edges) {
            if (distance[edge.u] + edge.w < distance[edge.v]) {
                distance[edge.v] = distance[edge.u] + edge.w;
            }
        }
    }

    for (const edge of edges) {
        if (distance[edge.u] + edge.w < distance[edge.v]) {
            console.log("Graph contains negative weight cycle");
            return;
        }
    }

    console.log("Vertex Distance from Source");
    for (let i = 0; i < V; ++i) {
        console.log(`${i}\t${distance[i]}`);
    }
}

// Example usage
let edges = [
    new Edge(0, 1, -1), new Edge(0, 2, 4),
    new Edge(1, 2, 3), new Edge(1, 3, 2),
    new Edge(1, 4, 2), new Edge(3, 2, 5),
    new Edge(3, 1, 1), new Edge(4, 3, -3)
];
let V = 5;
let src = 0;
bellmanFord(edges, V, src);
