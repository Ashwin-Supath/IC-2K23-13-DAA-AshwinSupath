# Algorithmic Analysis & Implementation Guide: Searching & Sorting

A comprehensive and technical README documenting the design, implementation, formal analysis, and empirical benchmarking of fundamental searching and sorting algorithms.

---

## Table of Contents
1. [Overview & Project Objectives](#overview--project-objectives)
2. [Searching Algorithms](#searching-algorithms)
   - [1. Linear Search](#1-linear-search)
   - [2. Binary Search (Iterative & Recursive)](#2-binary-search-iterative--recursive)
3. [Sorting Algorithms](#sorting-algorithms)
   - [3. Bubble Sort (Iterative & Recursive)](#3-bubble-sort-iterative--recursive)
   - [4. Selection Sort](#4-selection-sort)
   - [5. Insertion Sort (Iterative & Recursive)](#5-insertion-sort-iterative--recursive)
4. [Comparative Complexity Analysis](#comparative-complexity-analysis)
5. [Empirical Benchmarking & Performance Graphs](#empirical-benchmarking--performance-graphs)
6. [Key Learning Outcomes](#key-learning-outcomes)

---

## Overview & Project Objectives

Searching and sorting constitute the core computational building blocks in computer science. This documentation analyzes the theoretical efficiency and real-world behavior of five classical algorithms across both iterative and recursive paradigms:
- **Searching**: Linear Search, Binary Search (Iterative & Recursive)
- **Sorting**: Bubble Sort (Iterative & Recursive), Selection Sort, Insertion Sort (Iterative & Recursive)

---

## Searching Algorithms

### 1. Linear Search

#### Problem Statement
Given an array `arr` of `n` elements and a target key `x`, determine whether `x` is present in `arr`, and if so, return its index.

#### Algorithm / Approach
- Sequentially iterate through each element from index `0` to `n - 1`.
- Compare each element with the target value.
- Terminate early and return the index if a match is found.
- If the entire sequence is traversed without a match, report failure / `-1`.

#### Pseudocode & Flowchart

```text
FUNCTION LinearSearch(arr, target):
    FOR index FROM 0 TO length(arr) - 1 DO
        IF arr[index] == target THEN
            RETURN index
        END IF
    END FOR
    RETURN -1
END FUNCTION
```

```
       +--------------------+
       |       Start        |
       +---------+----------+
                 |
                 v
       +--------------------+
       |     index = 0      |
       +---------+----------+
                 |
    +----------->+
    |            |
    |            v
    |    /---------------\
    |   /   index < n ?   \--- No ---> [ Return -1 (Not Found) ]
    |   \                 /
    |    \---------------/
    |            | Yes
    |            v
    |    /---------------\
    |   / arr[idx] == target? \--- Yes --> [ Return index ]
    |   \                 /
    |    \---------------/
    |            | No
    |            v
    |     index = index + 1
    +------------+
```

#### Time & Space Complexity Analysis
- **Best-Case Time Complexity**: $\mathcal{O}(1)$ — Target is found at the first position.
- **Worst-Case Time Complexity**: $\mathcal{O}(n)$ — Target is at the end or absent.
- **Average-Case Time Complexity**: $\mathcal{O}(n)$ — Expected search space is $n / 2$.
- **Auxiliary Space Complexity**: $\mathcal{O}(1)$ — In-place scan requiring constant extra memory.

#### Sample Input / Output
- **Input**: `arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, `target = 5`
- **Output**: `5 is present in the list at index: 4`
- **Input**: `arr = [1, 2, 3, 4, 5]`, `target = 99`
- **Output**: `Element not found...!`

---

### 2. Binary Search (Iterative & Recursive)

#### Problem Statement
Given a **sorted** array `arr` of `n` elements and a target value `key`, locate the position of `key` within logarithmic time.

#### Algorithm / Approach
- **Divide-and-Conquer Strategy**:
  1. Define search bounds `low = 0` and `high = n - 1`.
  2. Compute middle index `mid = low + (high - low) // 2`.
  3. If `arr[mid] == key`, return `mid`.
  4. If `key < arr[mid]`, narrow search space to left sub-array: `high = mid - 1`.
  5. If `key > arr[mid]`, narrow search space to right sub-array: `low = mid + 1`.
  6. Repeat iteratively or recursively until `low > high`.

#### Pseudocode

**Iterative Variant:**
```text
FUNCTION BinarySearchIterative(arr, target):
    low = 0
    high = length(arr) - 1
    WHILE low <= high DO
        mid = low + (high - low) / 2
        IF arr[mid] == target THEN
            RETURN mid
        ELSE IF target < arr[mid] THEN
            high = mid - 1
        ELSE
            low = mid + 1
        END IF
    END WHILE
    RETURN -1
END FUNCTION
```

**Recursive Variant:**
```text
FUNCTION BinarySearchRecursive(arr, target, low, high):
    IF low > high THEN
        RETURN -1
    END IF
    mid = low + (high - low) / 2
    IF arr[mid] == target THEN
        RETURN mid
    ELSE IF target < arr[mid] THEN
        RETURN BinarySearchRecursive(arr, target, low, mid - 1)
    ELSE
        RETURN BinarySearchRecursive(arr, target, mid + 1, high)
    END IF
END FUNCTION
```

#### Time & Space Complexity Analysis
- **Best-Case Time Complexity**: $\mathcal{O}(1)$ — Target located at the root median element.
- **Worst-Case Time Complexity**: $\mathcal{O}(\log n)$ — Halving the search interval at each step ($T(n) = T(n/2) + \mathcal{O}(1)$).
- **Average-Case Time Complexity**: $\mathcal{O}(\log n)$.
- **Auxiliary Space Complexity**:
  - *Iterative*: $\mathcal{O}(1)$ — Constant pointers.
  - *Recursive*: $\mathcal{O}(\log n)$ — Call stack frames proportional to recursion depth.

#### Sample Input / Output
- **Input**: `arr = [20, 23, 45, 56, 66, 67, 78]`, `target = 45`
- **Output**: `The value is found at index: 2 (Value: 45)`
- **Input**: `arr = [20, 23, 45, 56, 66, 67, 78]`, `target = 100`
- **Output**: `-1 (Element not found)`

---

## Sorting Algorithms

### 3. Bubble Sort (Iterative & Recursive)

#### Problem Statement
Given an unsorted array `arr` of `n` elements, arrange the elements in non-decreasing order by repeatedly swapping adjacent out-of-order elements.

#### Algorithm / Approach
- Compare adjacent elements `(arr[j], arr[j+1])`.
- Swap them if `arr[j] > arr[j+1]`.
- After pass $i$, the largest element among unsorted items bubbles up to its final position at the end.
- *Recursive formulation*: Perform one linear pass to place the largest item at index $n-1$, then recursively invoke on sub-array of size $n-1$.

#### Pseudocode

**Iterative Variant:**
```text
FUNCTION BubbleSortIterative(arr):
    n = length(arr)
    FOR i FROM 0 TO n - 1 DO
        FOR j FROM 0 TO n - i - 2 DO
            IF arr[j] > arr[j + 1] THEN
                SWAP(arr[j], arr[j + 1])
            END IF
        END FOR
    END FOR
    RETURN arr
END FUNCTION
```

**Recursive Variant:**
```text
FUNCTION BubbleSortRecursive(arr, n, i):
    IF n == 1 THEN RETURN arr
    IF i == n - 1 THEN
        RETURN BubbleSortRecursive(arr, n - 1, 0)
    END IF
    IF arr[i] > arr[i + 1] THEN
        SWAP(arr[i], arr[i + 1])
    END IF
    RETURN BubbleSortRecursive(arr, n, i + 1)
END FUNCTION
```

#### Time & Space Complexity Analysis
- **Best-Case Time Complexity**: $\mathcal{O}(n)$ (with swapped flag) / $\mathcal{O}(n^2)$ standard.
- **Worst-Case Time Complexity**: $\mathcal{O}(n^2)$ — Reverse-sorted list requires $\frac{n(n-1)}{2}$ swaps.
- **Average-Case Time Complexity**: $\mathcal{O}(n^2)$.
- **Auxiliary Space Complexity**:
  - *Iterative*: $\mathcal{O}(1)$ in-place.
  - *Recursive*: $\mathcal{O}(n)$ due to activation stack depth.

#### Sample Input / Output
- **Input**: `arr = [26, 30, 12, 14, 60, 55]`
- **Output**: `[12, 14, 26, 30, 55, 60]`

---

### 4. Selection Sort

#### Problem Statement
Sort an unsorted array by repeatedly finding the minimum element from the unsorted segment and placing it at the beginning.

#### Algorithm / Approach
1. Partition the list into sorted prefix and unsorted suffix.
2. Search unsorted suffix `[i ... n-1]` for minimum value index `min_idx`.
3. Swap `arr[min_idx]` with `arr[i]`.
4. Increment sorted prefix boundary `i` and repeat.

#### Pseudocode & Flowchart

```text
FUNCTION SelectionSort(arr):
    n = length(arr)
    FOR i FROM 0 TO n - 1 DO
        min_idx = i
        FOR j FROM i + 1 TO n - 1 DO
            IF arr[j] < arr[min_idx] THEN
                min_idx = j
            END IF
        END FOR
        SWAP(arr[i], arr[min_idx])
    END FOR
    RETURN arr
END FUNCTION
```

```
       +-----------------------------+
       |   i = 0, min_idx = 0        |
       +--------------+--------------+
                      |
        +------------>+
        |             |
        |             v
        |      /---------------\
        |     /     i < n ?     \--- No ---> [ Array is Sorted ]
        |     \                 /
        |      \---------------/
        |             | Yes
        |             v
        |      Find min_idx in       
        |      sub-array [i...n-1]   
        |             |              
        |             v              
        |      SWAP(arr[i], arr[min])
        |             |              
        |      i = i + 1             
        +-------------+              
```

#### Time & Space Complexity Analysis
- **Best-Case Time Complexity**: $\mathcal{O}(n^2)$ — Always conducts $\frac{n(n-1)}{2}$ comparisons regardless of initial ordering.
- **Worst-Case Time Complexity**: $\mathcal{O}(n^2)$.
- **Average-Case Time Complexity**: $\mathcal{O}(n^2)$.
- **Auxiliary Space Complexity**: $\mathcal{O}(1)$ in-place.
- **Key Trait**: Minimizes memory writes (at most $n-1$ swaps throughout).

#### Sample Input / Output
- **Input**: `arr = [26, 30, 12, 14, 60, 55]`
- **Output**: `[12, 14, 26, 30, 55, 60]`

---

### 5. Insertion Sort (Iterative & Recursive)

#### Problem Statement
Build the sorted array one element at a time by consuming one input item per iteration and inserting it into its correct relative position within the already sorted prefix.

#### Algorithm / Approach
- Iterate through elements starting from index 1.
- Compare current item (`key` or `arr[j]`) backwards against sorted prefix.
- Shift larger elements one position to the right.
- Insert key when correct position is discovered.

#### Pseudocode

**Iterative Variant:**
```text
FUNCTION InsertionSortIterative(arr):
    FOR i FROM 1 TO length(arr) - 1 DO
        key = arr[i]
        j = i - 1
        WHILE j >= 0 AND arr[j] > key DO
            arr[j + 1] = arr[j]
            j = j - 1
        END WHILE
        arr[j + 1] = key
    END FOR
    RETURN arr
END FUNCTION
```

**Recursive Variant:**
```text
FUNCTION InsertionSortRecursive(arr, i, j):
    IF i >= length(arr) THEN RETURN arr
    IF j IS NULL THEN j = i
    
    IF j > 0 AND arr[j] < arr[j - 1] THEN
        SWAP(arr[j], arr[j - 1])
        RETURN InsertionSortRecursive(arr, i, j - 1)
    END IF
    
    RETURN InsertionSortRecursive(arr, i + 1, NULL)
END FUNCTION
```