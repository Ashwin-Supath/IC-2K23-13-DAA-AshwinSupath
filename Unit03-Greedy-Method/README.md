# Unit 3: Greedy Method

This unit explores the Greedy Method algorithmic paradigm. Greedy algorithms build up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit (the local optimum) with the hope that these local choices will lead to a globally optimal solution.

## 🗂️ Algorithms Implemented

### Core Greedy Algorithms
- [Fractional Knapsack](./Fractional-Knapsack/) - $O(N \log N)$ complexity, maximizes value by taking fractions of items based on value/weight ratios.
- [Job Scheduling with Deadlines](./Job-Scheduling/) - $O(N^2)$ complexity, maximizes profit by scheduling jobs in the latest possible available time slots before their deadlines.

### Greedy Graph Algorithms
- [Prim's Algorithm](./Prims-Algorithm/) - $O(V^2)$ complexity (matrix implementation), finds the Minimum Spanning Tree by growing a single tree vertex by vertex.
- [Kruskal's Algorithm](./Kruskals-Algorithm/) - $O(E \log E)$ complexity, finds the Minimum Spanning Tree by sorting edges and using a Disjoint Set to avoid cycles.
- [Dijkstra's Algorithm](./Dijkstras-Algorithm/) - $O(V^2)$ complexity (matrix implementation), finds the Single-Source Shortest Path to all other vertices.

