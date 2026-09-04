"""
Binary Search Algorithm (Iterative)
Approach: Repeatedly divide the search interval in half.
Precondition: The array must be sorted.
"""

def binary_search_iterative(arr, target):
    """
    Performs iterative binary search on a sorted array.

    Args:
        arr (list): Sorted list of elements.
        target: Element to search for.

    Returns:
        int: Index of target if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    arr = [11, 12, 22, 25, 45, 64, 90]
    target = 25

    print(f"Sorted Array: {arr}")
    print(f"Searching for: {target}")

    result = binary_search_iterative(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")


if __name__ == "__main__":
    main()