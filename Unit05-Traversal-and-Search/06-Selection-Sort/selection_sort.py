"""
Selection Sort Algorithm
Repeatedly selects the minimum element and places it at the beginning.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def main():
    arr = [64, 25, 12, 22, 11]
    print(f"Original: {arr}")
    print(f"Sorted: {selection_sort(arr.copy())}")


if __name__ == "__main__":
    main()