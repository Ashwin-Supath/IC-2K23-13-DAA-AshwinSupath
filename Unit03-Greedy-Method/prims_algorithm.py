import sys
from pathlib import Path
import random

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def prims_algorithm(graph):
    # graph is an adjacency matrix
    V = len(graph)
    if V == 0:
        return 0
        
    # Array to track selected vertices for MST
    selected = [False] * V
    
    # We need to track the number of edges to ensure we pick V-1 edges
    no_edge = 0
    selected[0] = True
    mst_weight = 0
    
    # Track the MST edges for V-1 iterations
    while no_edge < V - 1:
        minimum = float('inf')
        u = 0
        v = 0
        
        # Iterate over all selected vertices
        for i in range(V):
            if selected[i]:
                # Iterate over all adjacent vertices
                for j in range(V):
                    # If vertex j is not selected and there is an edge
                    if not selected[j] and graph[i][j]:  
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            u = i
                            v = j
                            
        # Add the selected edge to MST
        selected[v] = True
        mst_weight += graph[u][v]
        no_edge += 1
        
    return mst_weight

def generate_random_graph(v):
    # Generates a symmetric adjacency matrix for an undirected graph
    graph = [[0 for _ in range(v)] for _ in range(v)]
    for i in range(v):
        for j in range(i + 1, v):
            weight = random.randint(1, 100)
            graph[i][j] = weight
            graph[j][i] = weight
    return graph

if __name__ == "__main__":
    # O(V^2) complexity with an adjacency matrix requires moderate input sizes
    sizes = [100, 200, 300, 400, 500, 600, 700]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[prims_algorithm],
        sizes=sizes,
        data_generator=generate_random_graph,
        title="Prim's Algorithm Performance",
        ylabel="Time (seconds) - O(V^2)"
    )