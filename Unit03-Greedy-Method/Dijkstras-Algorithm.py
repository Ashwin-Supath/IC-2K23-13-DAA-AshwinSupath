import sys
from pathlib import Path
import random

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def dijkstras_algorithm(graph):
    # graph is an adjacency matrix
    V = len(graph)
    if V == 0:
        return 0
        
    # dist array holds the shortest distance from source to i
    dist = [float('inf')] * V
    
    # spt_set (shortest path tree set) tracks vertices whose minimum distance is finalized
    spt_set = [False] * V
    
    # Source vertex is always 0 for this test
    src = 0
    dist[src] = 0
    
    for _ in range(V):
        # Pick the minimum distance vertex from the set of vertices not yet processed
        min_dist = float('inf')
        u = -1
        
        for v in range(V):
            if dist[v] < min_dist and not spt_set[v]:
                min_dist = dist[v]
                u = v
                
        # If all remaining vertices are unreachable, break
        if u == -1:
            break
            
        # Mark the picked vertex as processed
        spt_set[u] = True
        
        # Update dist value of the adjacent vertices of the picked vertex
        for v in range(V):
            if graph[u][v] > 0 and not spt_set[v] and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                
    # Return the sum of all shortest paths from the source to avoid returning a massive array
    return sum(d for d in dist if d != float('inf'))

def generate_random_graph(v):
    # Generates a symmetric adjacency matrix for an undirected graph with positive weights
    graph = [[0 for _ in range(v)] for _ in range(v)]
    for i in range(v):
        for j in range(i + 1, v):
            # 20% chance of no direct edge (0) to simulate a more realistic graph
            if random.random() > 0.2:
                weight = random.randint(1, 100)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph

if __name__ == "__main__":
    # O(V^2) complexity requires moderate input sizes
    sizes = [100, 200, 300, 400, 500, 600, 700]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[dijkstras_algorithm],
        sizes=sizes,
        data_generator=generate_random_graph,
        title="Dijkstra's Algorithm Performance",
        ylabel="Time (seconds) - O(V^2)"
    )