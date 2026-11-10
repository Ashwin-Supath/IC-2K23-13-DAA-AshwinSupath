def insertion_s(arr):
    sorted=[]
    for i in range(0,len(arr)-1):
        if arr[i+1]<arr[i]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            sorted.append(arr[i])
        else:
            sorted.append(arr[i])
    return sorted
l=[3,5,6,7,2,66,43,21]
sort=insertion_s(l)
print(sort)