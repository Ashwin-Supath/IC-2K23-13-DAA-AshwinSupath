# Recursive Insertion Sort

## Problem Statement
Sort an array using Insertion Sort implemented recursively.

## Algorithm / Approach
1. Recursively sort the first n-1 elements.
2. Once the first n-1 elements are sorted, insert the nth element
   into its correct position among them (same shifting logic as
   iterative insertion sort).
3. Base case: an array of size 1 (or 0) is already sorted.

## Pseudocode

RECURSIVE_INSERTION_SORT(arr, n):
if n <= 1: return
RECURSIVE_INSERTION_SORT(arr, n-1)
key = arr[n-1]
j = n-2
while j >= 0 and arr[j] > key:
arr[j+1] = arr[j]
j = j - 1
arr[j+1] = key


## Time & Space Complexity
| Case | Time | Space |
|------|------|-------|
| Best | O(n) | O(n) |
| Average | O(n²) | O(n) |
| Worst | O(n²) | O(n) |

Space is O(n) due to recursion call stack depth (vs O(1) for iterative
insertion sort).

## Sample Input / Output

Input: [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]


## Learning Outcomes
- Converted iterative insertion logic into a recursive structure.
- Understood the trade-off: same time complexity as iterative version,
  but extra O(n) space due to recursion stack.