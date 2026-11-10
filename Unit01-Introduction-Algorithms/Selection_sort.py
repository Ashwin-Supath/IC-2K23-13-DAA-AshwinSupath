def slct_s(arr):
    n=len(arr)
    for i in range(0,len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
arr=[26, 30, 12, 14, 60, 55]
l=slct_s(arr)
print(l)
