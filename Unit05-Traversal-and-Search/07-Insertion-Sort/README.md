# Insertion Sort

## Problem Statement
Sort an array of n elements in ascending order using Insertion Sort.

## Algorithm / Approach
1. Start from the second element (index 1), treat first element as sorted.
2. Take the current element (`key`) and compare it with elements before it.
3. Shift all larger elements one position to the right.
4. Insert `key` into its correct position.
5. Repeat for all elements.

## Pseudocode
INSERTION_SORT(arr):
for i = 1 to n-1:
key = arr[i]
j = i - 1
while j >= 0 and arr[j] > key:
arr[j+1] = arr[j]
j = j - 1
arr[j+1] = key


## Time & Space Complexity
| Case | Time | Explanation |
|------|------|-------------|
| Best | O(n) | Array already sorted, inner loop never runs |
| Average | O(n²) | Random order |
| Worst | O(n²) | Reverse sorted, max shifting |

**Space:** O(1) — in-place sorting.
**Note:** Efficient for small or nearly-sorted datasets; used internally
by hybrid algorithms like Timsort for small partitions.

## Sample Input / Output

Input: [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]


## Learning Outcomes
- Understood the "insert into sorted portion" technique.
- Learned why Insertion Sort performs well on nearly-sorted data
  (best case O(n)), unlike Selection Sort.