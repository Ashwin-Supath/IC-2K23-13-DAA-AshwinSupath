"""
Binary Search Algorithm (Recursive)
Precondition: array must be sorted.
"""

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def main():
    arr = [11, 12, 22, 25, 45, 64, 90]
    target = 45
    result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Result: Found at index {result}" if result != -1 else "Not found")


if __name__ == "__main__":
    main()