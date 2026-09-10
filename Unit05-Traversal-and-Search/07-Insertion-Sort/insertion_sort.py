"""
Insertion Sort Algorithm
Builds the sorted array one element at a time by inserting each
element into its correct position among the already-sorted part.
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    arr = [64, 25, 12, 22, 11]
    print(f"Original: {arr}")
    print(f"Sorted: {insertion_sort(arr.copy())}")


if __name__ == "__main__":
    main()