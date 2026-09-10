# Selection Sort

## Problem Statement
Sort an array of n elements in ascending order using Selection Sort.

## Algorithm / Approach
1. Find the minimum element in the unsorted part of the array.
2. Swap it with the first element of the unsorted part.
3. Move the boundary of sorted/unsorted part one step forward.
4. Repeat until the array is fully sorted.

## Pseudocode
SELECTION_SORT(arr):
for i = 0 to n-2:
min_idx = i
for j = i+1 to n-1:
if arr[j] < arr[min_idx]: min_idx = j
swap(arr[i], arr[min_idx])


## Time & Space Complexity
| Case | Time | Explanation |
|------|------|-------------|
| Best | O(n²) | Still scans full unsorted part every time |
| Average | O(n²) | No early exit possible |
| Worst | O(n²) | Reverse sorted |

**Space:** O(1) — in-place sorting.
**Note:** Unlike Bubble Sort, Selection Sort has no best-case speedup —
it always does the same number of comparisons.

## Sample Input / Output

Input: [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]

## Learning Outcomes
- Understood selection-based sorting: minimum finding + swapping.
- Learned why Selection Sort makes fewer swaps than Bubble Sort
  (only n-1 swaps total) but same number of comparisons.