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

nums = [38, 27, 43, 3, 9, 82, 10]
print("Original:", nums)
print("Quick Sorted:", quick_sort(nums))
