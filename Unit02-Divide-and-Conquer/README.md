# Unit 02: Divide and Conquer Algorithms

A concise technical guide covering the Divide-and-Conquer design paradigm, implementations, recurrence relations, complexity analysis, and empirical benchmarking for **Merge Sort** and **Quick Sort**.

---

## 1. Overview & Paradigm

The **Divide-and-Conquer** technique solves a problem recursively in three steps:
1. **Divide**: Partition the problem into smaller, disjoint subproblems.
2. **Conquer**: Solve the subproblems recursively (or directly at base case $n \le 1$).
3. **Combine**: Merge subproblem solutions into the final solution.

```
                     [ Input Array (Size n) ]
                                |
               +----------------+----------------+
               | Divide                          | Divide
               v                                 v
        [ Left Subarray ]                [ Right Subarray ]
               |                                 |
         Conquer (Recurse)                 Conquer (Recurse)
               \                                 /
                +----------------+--------------+
                                 | Combine / Merge
                                 v
                        [ Fully Sorted Array ]
```

---

## 2. Algorithms & Implementation

### 1. Merge Sort

- **Approach**: Splits array in half recursively, then merges the sorted halves using a two-pointer technique.
- **Source File**: [`Merge_sort.py`](Merge_sort.py)

#### Core Logic
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr
```

#### Recurrence & Complexity
- **Recurrence**: $T(n) = 2T(n/2) + \Theta(n)$
- **By Master Theorem**: Case 2 ($a = 2, b = 2, c = 1 \implies \log_b a = c$) $\implies \mathbf{\Theta(n \log n)}$
- **Time Complexity**:
  - Best Case: $\mathcal{O}(n \log n)$
  - Average Case: $\mathcal{O}(n \log n)$
  - Worst Case: $\mathcal{O}(n \log n)$
- **Space Complexity**: $\mathcal{O}(n)$ auxiliary array buffer + $\mathcal{O}(\log n)$ call stack.
- **Stability**: **Stable** (preserves original order of duplicates via `<=` in merge).

---

### 2. Quick Sort (Lomuto Partition)

- **Approach**: Selects the last element as pivot (`arr[h]`). Scans and swaps all elements $\le \text{pivot}$ to the left, places pivot at index $i+1$, then recurses on both partitions.
- **Source File**: [`Quick_sort.py`](Quick_sort.py)

#### Core Logic
```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    return arr

def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1
```

#### Recurrence & Complexity
- **Best / Balanced Partition**: $T(n) = 2T(n/2) + \Theta(n) \implies \mathbf{\mathcal{O}(n \log n)}$
- **Worst / Skewed Partition**: $T(n) = T(n-1) + \Theta(n) \implies \mathbf{\mathcal{O}(n^2)}$ (occurs on already sorted input with terminal pivot).
- **Average Case**: $\mathbf{\mathcal{O}(n \log n)}$
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary data space (in-place) + $\mathcal{O}(\log n)$ avg stack ($\mathcal{O}(n)$ worst).
- **Stability**: **Unstable** (due to non-adjacent swaps).

---

## 3. Sample Execution Trace

Given `nums = [38, 27, 43, 3, 9, 82, 10]`:

### Merge Sort Breakdown
```
Split:     [38, 27, 43]                      [3, 9, 82, 10]
Split:  [38]     [27, 43]                 [3, 9]        [82, 10]
Merge:  [38] + [27, 43] -> [27, 38, 43]   [3, 9] + [10, 82] -> [3, 9, 10, 82]
Final:  Merge([27, 38, 43], [3, 9, 10, 82]) -> [3, 9, 10, 27, 38, 43, 82]
```

### Quick Sort (First Partition Pass)
- Input: `[38, 27, 43, 3, 9, 82, 10]`, `pivot = 10`, `i = -1`
- `j = 3` (val `3` $\le 10$): swap `arr[0]` $\leftrightarrow$ `arr[3]` $\to [3, 27, 43, 38, 9, 82, 10]$, $i = 0$
- `j = 4` (val `9` $\le 10$): swap `arr[1]` $\leftrightarrow$ `arr[4]` $\to [3, 9, 43, 38, 27, 82, 10]$, $i = 1$
- Final Swap: `arr[i+1]` $\leftrightarrow$ `arr[h]` (swap `arr[2]=43` and `arr[6]=10`)
- Partitioned State: `[3, 9, 10, 38, 27, 82, 43]`, pivot fixed at index `2`.

**Output for both**: `[3, 9, 10, 27, 38, 43, 82]`

---

## 4. Comparison: Merge Sort vs. Quick Sort

| Feature | Merge Sort | Quick Sort (Lomuto) |
|:---|:---:|:---:|
| **Best-Case Time** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ |
| **Average-Case Time** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ |
| **Worst-Case Time** | $\mathcal{O}(n \log n)$ (Guaranteed) | $\mathcal{O}(n^2)$ |
| **Auxiliary Data Space** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ (In-place) |
| **Stack Space** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ avg / $\mathcal{O}(n)$ worst |
| **Stability** | Yes (Stable) | No (Unstable) |
| **Cache Locality** | Lower (allocates new buffers) | High (sequential scans in-place) |
| **Preferred Use** | Linked lists, external data, stability needed | General in-memory array sorting |

---

## 5. Benchmarking

The root utility [`Complexity_analyser.py`](../Complexity_analyser.py) evaluates runtime across increasing values of $N$:

```bash
# Run the benchmark engine from project root
python3 Complexity_analyser.py
```

- **Key Takeaway**: While both average $\mathcal{O}(n \log n)$, Quick Sort runs faster in practice on contiguous arrays due to superior cache locality and zero buffer allocation overhead.
