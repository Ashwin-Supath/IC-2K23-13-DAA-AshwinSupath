# Algorithm Performance Analyzer

## Problem Statement
Develop a tool that compares theoretical time complexity with actual
(experimental) execution time of different sorting algorithms across
varying input sizes.

## Algorithm / Approach
1. Generate random arrays of increasing sizes (100 to 5000 elements).
2. For each algorithm (Bubble, Selection, Insertion, Merge, Quick Sort),
   measure execution time using Python's `time.perf_counter()`.
3. Store results in a CSV file for record-keeping.
4. Plot Execution Time vs Input Size for all algorithms on a single graph
   using matplotlib.

## Time & Space Complexity (Theoretical, for reference)
| Algorithm | Best | Average | Worst |
|-----------|------|---------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |

## Sample Output
Console prints execution time for each algorithm at each input size.
Results are also saved to:
- `performance_results.csv` — raw timing data
- `performance_graph.png` — visual comparison graph

## Experimental Results
See `performance_results.csv` and `performance_graph.png` in this folder.
As expected, O(n²) algorithms (Bubble, Selection, Insertion) show a
sharp upward curve as input size grows, while O(n log n) algorithms
(Merge, Quick) scale far more gradually — confirming theoretical
complexity analysis with real execution data.

## Learning Outcomes
- Learned to empirically measure and compare algorithm performance.
- Validated theoretical Big-O predictions against real execution times.
- Understood how constant factors and input size affect real-world
  performance, not just asymptotic complexity.
- Gained experience visualizing performance data using matplotlib.
