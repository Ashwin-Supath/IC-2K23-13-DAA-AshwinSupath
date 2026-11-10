def insertion_s(arr, i=1, j=None):
    if i >= len(arr):
        return arr

    if j is None:
        j = i

    if j > 0 and arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]

        return insertion_s(arr, i, j - 1)

    return insertion_s(arr, i + 1, None)


l = [3, 5, 6, 7, 2, 66, 43, 21]

sort = insertion_s(l)

print(sort)