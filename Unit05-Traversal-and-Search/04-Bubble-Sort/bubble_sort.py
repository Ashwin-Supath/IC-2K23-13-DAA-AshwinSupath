"""
Bubble Sort Algorithm (Iterative)
Repeatedly swaps adjacent elements if they are in wrong order.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def main():
    arr = [64, 25, 12, 22, 11]
    print(f"Original: {arr}")
    print(f"Sorted: {bubble_sort(arr.copy())}")


if __name__ == "__main__":
    main()