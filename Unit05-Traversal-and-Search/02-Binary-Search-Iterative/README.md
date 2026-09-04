# Binary Search (Iterative)

## Problem Statement
Given a sorted array of `n` elements and a target value, find the index of
the target element using Binary Search (iterative approach). If the element
is not present, return -1.

## Algorithm / Approach
1. Set `low = 0` and `high = n - 1`.
2. While `low <= high`:
   - Calculate `mid = (low + high) / 2`.
   - If `arr[mid] == target`, return `mid`.
   - If `arr[mid] < target`, search the right half: `low = mid + 1`.
   - If `arr[mid] > target`, search the left half: `high = mid - 1`.
3. If the loop ends without a match, return -1.

## Pseudocode

BINARY_SEARCH_ITERATIVE(arr, target):
low = 0
high = length(arr) - 1
while low <= high:
mid = (low + high) / 2
if arr[mid] == target:
return mid
else if arr[mid] < target:
low = mid + 1
else:
high = mid - 1
return -1


## Time & Space Complexity
| Case         | Time Complexity | Explanation                                   |
|--------------|-----------------|-------------------------------------------------|
| Best Case    | O(1)             | Target found at the middle on first check      |
| Average Case | O(log n)         | Search space halves each iteration              |
| Worst Case   | O(log n)         | Target at boundary or not present               |

**Space Complexity:** O(1) — only a few variables used, no recursion stack.

## Sample Input / Output
Input:
arr = [11, 12, 22, 25, 45, 64, 90]
target = 25

Output:
Element found at index 3



## Learning Outcomes
- Understood how dividing the search space repeatedly reduces time
  complexity from O(n) to O(log n).
- Learned the importance of the array being sorted for Binary Search
  to work correctly.
- Understood the iterative approach avoids recursion overhead
  (no extra call stack space).
  