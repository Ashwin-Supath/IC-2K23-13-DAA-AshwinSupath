import sys
from pathlib import Path
import random

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def fractional_knapsack(items):
    # Dynamically set capacity to half of the total weight for the test
    capacity = sum(weight for value, weight in items) // 2
    
    # Sort items based on value/weight ratio in descending order
    # Python's Timsort operates in O(N log N)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0.0
    for value, weight in items:
        if capacity >= weight:
            # Take the whole item
            capacity -= weight
            total_value += value
        else:
            # Take the fractional part of the item to fill the remaining capacity
            total_value += value * (capacity / weight)
            break
            
    return total_value

if __name__ == "__main__":
    sizes = [1000, 5000, 10000, 20000, 30000, 40000, 50000]
    
    # Generate a list of (value, weight) tuples. Avoid weight=0 to prevent division by zero.
    data_generator = lambda n: [(random.randint(10, 500), random.randint(1, 100)) for _ in range(n)]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[fractional_knapsack],
        sizes=sizes,
        data_generator=data_generator,
        title="Fractional Knapsack Performance",
        ylabel="Time (seconds) - O(N log N)"
    )