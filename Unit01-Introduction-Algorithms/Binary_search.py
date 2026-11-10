def binary_s(lst, tar):
    start=0
    end=len(lst)-1

    while start<=end:
        mid=int((start+ end)/2)
        if tar==lst[mid]:
            return lst[mid]
        elif tar<lst[mid]:
            end=mid-1
        else:
            start=mid+1

l1=[20,23,45,56,66,67,78]
search=binary_s(l1,100)
print("The value is found",search)