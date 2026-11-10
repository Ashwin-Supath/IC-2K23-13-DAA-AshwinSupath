def binary_s(lst, a, start, end):
    if start > end:
        return -1
    mid = int((start + end) /2)
    if a == lst[mid]:
        return lst[mid]

    elif a < lst[mid]:
        return binary_s(lst, a, start, mid - 1)

    else:
        return binary_s(lst, a, mid + 1, end)

l1=[20,23,45,56,66,67,78]
search=binary_s(l1,45,0,len(l1)-1)
print("The value is found",search)