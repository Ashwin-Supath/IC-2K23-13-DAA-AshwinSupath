# Merge Sort

## Problem Statement
Sort an array of n elements in ascending order using Merge Sort
(Divide and Conquer approach).

## Algorithm / Approach
1. **Divide:** Split the array into two halves.
2. **Conquer:** Recursively sort each half.
3. **Combine:** Merge the two sorted halves into one sorted array by
   comparing elements from both halves and picking the smaller one
   each time.
4. Base case: an array of size 0 or 1 is already sorted.

## Pseudocode
MERGE_SORT(arr):
if length(arr) <= 1: return arr
mid = length(arr) / 2
left = MERGE_SORT(arr[0:mid])
right = MERGE_SORT(arr[mid:end])
return MERGE(left, right)

MERGE(left, right):
result = []
while left and right not empty:
if left[0] <= right[0]: append left[0] to result, remove from left
else: append right[0] to result, remove from right
append remaining elements of left and right to result
return result


## Time & Space Complexity
| Case | Time | Explanation |
|------|------|-------------|
| Best | O(n log n) | Always divides and merges regardless of input |
| Average | O(n log n) | Consistent performance |
| Worst | O(n log n) | Guaranteed, no bad-case degradation |

**Space Complexity:** O(n) — requires extra arrays for merging
(not in-place, unlike Quick Sort).

**Recurrence Relation:** T(n) = 2T(n/2) + O(n) → O(n log n) by
Master Theorem.

## Sample Input / Output
Input: [64, 25, 12, 22, 11, 90, 45]
Output: [11, 12, 22, 25, 45, 64, 90]


## Learning Outcomes
- Understood the Divide and Conquer paradigm in practice.
- Learned how the merge step combines two sorted arrays in O(n).
- Understood why Merge Sort guarantees O(n log n) in all cases,
  unlike Quick Sort's worst-case O(n²).
- Learned the space trade-off: O(n) extra space vs in-place sorts.