import sys
from pathlib import Path
import random
import copy

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def floyd_warshall(graph):
    V = len(graph)
    # Create a copy of the graph to serve as our distance DP table
    # dist[i][j] will hold the shortest distance from vertex i to vertex j
    dist = copy.deepcopy(graph)
    
    # k is the intermediate vertex
    for k in range(V):
        # i is the source vertex
        for i in range(V):
            # j is the destination vertex
            for j in range(V):
                # If vertex k is on the shortest path from i to j, update the distance
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
    return dist

def generate_graph(v):
    # Generates a directed adjacency matrix
    graph = [[float('inf') for _ in range(v)] for _ in range(v)]
    for i in range(v):
        graph[i][i] = 0  # Distance to itself is 0
        for j in range(v):
            if i != j:
                # 70% chance of a directed edge existing
                if random.random() < 0.7:
                    graph[i][j] = random.randint(1, 50)
    return graph

if __name__ == "__main__":
    # Small sizes are required because O(V^3) grows extremely fast
    sizes = [20, 50, 80, 110, 140, 170, 200]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[floyd_warshall],
        sizes=sizes,
        data_generator=generate_graph,
        title="Floyd-Warshall Algorithm Performance",
        ylabel="Time (seconds) - O(V^3)"
    )