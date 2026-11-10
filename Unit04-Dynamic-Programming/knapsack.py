import sys
from pathlib import Path
import random

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def knapsack_01(data):
    items, capacity = data
    n = len(items)
    
    # Create a 2D array K[][] to store the maximum value at each n and w
    K = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table K[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            # items[i-1][1] is the weight, items[i-1][0] is the value
            elif items[i-1][1] <= w:
                K[i][w] = max(items[i-1][0] + K[i-1][w - items[i-1][1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
                
    return K[n][capacity]

def generate_knapsack_data(n):
    # Scale capacity proportionally to n so the O(N * W) curve is visible
    capacity = n * 10
    # items is a list of (value, weight) tuples
    items = [(random.randint(10, 100), random.randint(1, 30)) for _ in range(n)]
    return (items, capacity)

if __name__ == "__main__":
    # Moderate input sizes due to the O(N * W) space and time requirements
    sizes = [50, 100, 200, 300, 400, 500, 600]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[knapsack_01],
        sizes=sizes,
        data_generator=generate_knapsack_data,
        title="0-1 Knapsack (DP) Performance",
        ylabel="Time (seconds) - O(N * W)"
    )