"""
Linear Search Algorithm
Approach: Sequentially check each element of the list until
a match is found or the list ends.
"""

def linear_search(arr, target):
    """
    Performs linear search on arr to find target.

    Args:
        arr (list): List of elements to search in.
        target: Element to search for.

    Returns:
        int: Index of target if found, else -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


def main():
    arr = [64, 25, 12, 22, 11, 90, 45]
    target = 22

    print(f"Array: {arr}")
    print(f"Searching for: {target}")

    result = linear_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")


if __name__ == "__main__":
    main()