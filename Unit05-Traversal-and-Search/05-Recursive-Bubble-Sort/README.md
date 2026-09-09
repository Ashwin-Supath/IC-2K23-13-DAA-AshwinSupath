# Recursive Bubble Sort

## Problem Statement
Sort an array using Bubble Sort implemented recursively.

## Algorithm / Approach
For a given size n, do one pass of bubbling the largest element to the
end, then recursively sort the remaining n-1 elements.

## Pseudocode
RECURSIVE_BUBBLE_SORT(arr, n):
if n == 1: return
for i = 0 to n-2:
if arr[i] > arr[i+1]: swap(arr[i], arr[i+1])
RECURSIVE_BUBBLE_SORT(arr, n-1)


## Time & Space Complexity
| Case | Time | Space |
|------|------|-------|
| Best | O(n²)* | O(n) |
| Average | O(n²) | O(n) |
| Worst | O(n²) | O(n) |

*Without swap-flag optimization, even best case stays O(n²) here.
Space is O(n) due to recursion call stack (vs O(1) for iterative).

## Sample Input / Output

Input: [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]


## Learning Outcomes
- Converted an iterative sort into a recursive version.
- Understood recursion adds O(n) space overhead vs iterative O(1).