# Bubble Sort

## Problem Statement
Sort an array of n elements in ascending order using Bubble Sort.

## Algorithm / Approach
Repeatedly step through the array, compare adjacent elements, swap them
if in wrong order. Repeat until no swaps are needed.

## Pseudocode
BUBBLE_SORT(arr):
for i = 0 to n-2:
for j = 0 to n-2-i:
if arr[j] > arr[j+1]: swap(arr[j], arr[j+1])


## Time & Space Complexity
| Case | Time | Explanation |
|------|------|-------------|
| Best | O(n) | Already sorted (with swapped flag optimization) |
| Average | O(n²) | Random order |
| Worst | O(n²) | Reverse sorted |

**Space:** O(1) — in-place sorting.

## Sample Input / Output

Input: [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]


## Learning Outcomes
- Understood adjacent-element comparison based sorting.
- Learned the "swapped" flag optimization for best-case O(n).