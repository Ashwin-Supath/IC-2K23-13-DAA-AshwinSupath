def b_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
    
arr=[26, 30, 12, 14, 60, 55]
l=b_sort(arr)
print(l)
