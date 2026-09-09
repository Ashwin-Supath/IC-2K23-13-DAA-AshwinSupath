"""
Recursive Bubble Sort
Base case: if array size is 1, it's already sorted.
"""

def recursive_bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return recursive_bubble_sort(arr, n - 1)


def main():
    arr = [64, 25, 12, 22, 11]
    print(f"Original: {arr}")
    print(f"Sorted: {recursive_bubble_sort(arr.copy())}")


if __name__ == "__main__":
    main()