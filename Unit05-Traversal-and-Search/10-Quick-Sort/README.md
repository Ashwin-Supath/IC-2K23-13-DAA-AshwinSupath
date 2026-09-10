# Quick Sort

## Problem Statement
Sort an array of n elements in ascending order using Quick Sort
(Divide and Conquer approach).

## Algorithm / Approach
1. **Choose a pivot** (here, the last element of the sub-array).
2. **Partition:** Rearrange the array so all elements smaller than
   the pivot come before it, and all larger elements come after it.
   The pivot is now in its final sorted position.
3. **Recurse:** Apply the same process to the sub-arrays on the left
   and right of the pivot.
4. Base case: a sub-array of size 0 or 1 is already sorted.

## Pseudocode
QUICK_SORT(arr, low, high):
if low < high:
pivot_index = PARTITION(arr, low, high)
QUICK_SORT(arr, low, pivot_index - 1)
QUICK_SORT(arr, pivot_index + 1, high)

PARTITION(arr, low, high):
pivot = arr[high]
i = low - 1
for j = low to high - 1:
if arr[j] <= pivot:
i = i + 1
swap(arr[i], arr[j])
swap(arr[i+1], arr[high])
return i + 1


## Time & Space Complexity
| Case | Time | Explanation |
|------|------|-------------|
| Best | O(n log n) | Pivot splits array into two equal halves |
| Average | O(n log n) | Random pivot placement |
| Worst | O(n²) | Already sorted array with poor pivot choice (e.g. last element on sorted input) |

**Space Complexity:** O(log n) average (recursion stack), O(n) worst case.
Sorting is **in-place** (no extra array needed, unlike Merge Sort).

**Recurrence Relation (average case):** T(n) = 2T(n/2) + O(n) → O(n log n)

## Sample Input / Output

Input: [64, 25, 12, 22, 11, 90, 45]
Output: [11, 12, 22, 25, 45, 64, 90]


## Learning Outcomes
- Understood the partitioning technique and how pivot placement works.
- Learned why Quick Sort's worst case (O(n²)) happens on already-sorted
  or reverse-sorted arrays with naive pivot selection.
- Compared Quick Sort (in-place, O(log n) space) vs Merge Sort
  (extra O(n) space) — a key trade-off in sorting algorithm design.
- Understood why Quick Sort is generally faster in practice despite
  worse worst-case complexity (better cache locality, smaller constants).
  