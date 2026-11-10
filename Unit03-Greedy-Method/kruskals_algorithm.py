import sys
from pathlib import Path
import random

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def kruskals_algorithm(data):
    V, edges = data
    
    # Sort edges based on their weight
    edges.sort(key=lambda item: item[2])
    
    # Disjoint Set data structure arrays
    parent = [i for i in range(V)]
    rank = [0] * V
    
    def find(i):
        if parent[i] == i:
            return i
        # Path compression
        parent[i] = find(parent[i])
        return parent[i]
        
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        
        # Union by rank
        if rank[root_i] < rank[root_j]:
            parent[root_i] = root_j
        elif rank[root_i] > rank[root_j]:
            parent[root_j] = root_i
        else:
            parent[root_j] = root_i
            rank[root_i] += 1
            
    mst_weight = 0
    edges_included = 0
    i = 0
    
    # MST contains exactly V-1 edges
    while edges_included < V - 1 and i < len(edges):
        u, v, weight = edges[i]
        i += 1
        
        x = find(u)
        y = find(v)
        
        # If including this edge does not cause a cycle
        if x != y:
            edges_included += 1
            mst_weight += weight
            union(x, y)
            
    return mst_weight

def generate_edge_list(v):
    edges = []
    # Generating a dense graph to ensure connectivity
    for i in range(v):
        for j in range(i + 1, v):
            edges.append((i, j, random.randint(1, 100)))
    return (v, edges)

if __name__ == "__main__":
    sizes = [100, 200, 300, 400, 500, 600, 700]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[kruskals_algorithm],
        sizes=sizes,
        data_generator=generate_edge_list,
        title="Kruskal's Algorithm Performance",
        ylabel="Time (seconds) - O(E log E)"
    )