# Binary Search (Recursive)

## Problem Statement
Find target's index in a sorted array using recursive Binary Search.

## Algorithm / Approach
Same as iterative binary search, but the halving step is done via
recursive function calls instead of a loop.

## Pseudocode
BINARY_SEARCH_RECURSIVE(arr, target, low, high):
if low > high: return -1
mid = (low + high) / 2
if arr[mid] == target: return mid
if arr[mid] < target: return BINARY_SEARCH_RECURSIVE(arr, target, mid+1, high)
return BINARY_SEARCH_RECURSIVE(arr, target, low, mid-1)


## Time & Space Complexity
| Case | Time | Space |
|------|------|-------|
| Best | O(1) | O(log n) |
| Average | O(log n) | O(log n) |
| Worst | O(log n) | O(log n) |

Space is O(log n) due to recursion call stack (unlike iterative O(1)).

## Sample Input / Output
Input: arr = [11, 12, 22, 25, 45, 64, 90], target = 45
Output: Found at index 4


## Learning Outcomes
- Understood recursive divide-and-conquer implementation.
- Compared recursion stack overhead vs iterative approach.

