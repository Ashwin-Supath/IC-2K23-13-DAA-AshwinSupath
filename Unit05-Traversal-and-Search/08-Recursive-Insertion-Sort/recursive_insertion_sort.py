"""
Recursive Insertion Sort
Base case: array of size 1 is already sorted.
Recursively sorts first n-1 elements, then inserts the nth element
into its correct position.
"""

def recursive_insertion_sort(arr, n=None):
    if n is None:
        n = len(arr)

    if n <= 1:
        return arr

    recursive_insertion_sort(arr, n - 1)

    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

    return arr


def main():
    arr = [64, 25, 12, 22, 11]
    print(f"Original: {arr}")
    print(f"Sorted: {recursive_insertion_sort(arr.copy())}")


if __name__ == "__main__":
    main()