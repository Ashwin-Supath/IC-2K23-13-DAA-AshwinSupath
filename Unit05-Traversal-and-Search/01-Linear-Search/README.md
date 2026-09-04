# Linear Search

## Problem Statement
Given an array of `n` elements and a target value, find the index of the
target element in the array using Linear Search. If the element is not
present, return -1.

## Algorithm / Approach
1. Start from the first element of the array.
2. Compare the current element with the target value.
3. If it matches, return the current index.
4. If not, move to the next element.
5. Repeat until the element is found or the array ends.
6. If the end of the array is reached without a match, return -1.

## Pseudocode

LINEAR_SEARCH(arr, target):
for i = 0 to length(arr) - 1:
if arr[i] == target:
return i
return -1


## Time & Space Complexity
| Case         | Time Complexity | Explanation                              |
|--------------|-----------------|-------------------------------------------|
| Best Case    | O(1)             | Target found at the first index          |
| Average Case | O(n)             | Target found somewhere in the middle     |
| Worst Case   | O(n)             | Target at last index or not present      |

**Space Complexity:** O(1) — no extra space used apart from input.

## Sample Input / Output

Input:
arr = [64, 25, 12, 22, 11, 90, 45]
target = 22

Output:
Element found at index 3



## Learning Outcomes
- Understood the working of a simple sequential search algorithm.
- Learned to analyze best, average, and worst-case time complexity.
- Understood why Linear Search is inefficient for large sorted datasets
  compared to Binary Search.