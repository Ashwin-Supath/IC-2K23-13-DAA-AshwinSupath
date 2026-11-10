# IC-2K23-13-DAA--Ashwin-Supath-
# Design and Analysis of Algorithms (DAA) Lab

This repository contains my laboratory assignments and implementations for the Design and Analysis of Algorithms course. All algorithms are implemented in Python and feature a custom benchmarking engine to dynamically compare theoretical time complexity against experimental hardware execution times.
## Table of Contents

| Unit | Topic | Concepts / Algorithms Used | Link |
|------|-------|----------------------------|------|
| **Unit 1** | Sorting & Structures | Bubble, Selection, Insertion, Radix Sort, Min-Heap | [View Unit](./Unit01-Introduction-Algorithms/) |
| **Unit 1** | Searching Algorithms | Linear Search, Binary Search | [View Unit](./Unit01-Introduction-Algorithms/) |
| **Unit 2** | Divide and Conquer | Merge Sort, Quick Sort | [View Unit](./Unit02-Divide-and-Conquer/) |
| **Unit 3** | Greedy Method | Fractional Knapsack, Job Scheduling with Deadlines | [View Unit](./Unit03-Greedy-Method/) |
| **Unit 3** | Greedy Graph Algorithms | Prim's, Kruskal's, Dijkstra's (Single-Source) | [View Unit](./Unit03-Greedy-Method/) |
| **Unit 4** | Dynamic Programming | 0/1 Knapsack, Floyd-Warshall (All-Pairs) | [View Unit](./Unit04-Dynamic-Programming/) |

## Setup & Requirements
- Python 3.8+
- Required packages for performance visualization: `pip install matplotlib`
- The repository uses a shared benchmarking engine (`Complexity_analyser.py`) located at the root.
- To run any algorithm and view its complexity graph, navigate to its specific folder and execute the Python file.

**Example:**
```bash
cd Unit01-Introduction-Algorithms/Bubble-Sort
python bubble_sort.py
