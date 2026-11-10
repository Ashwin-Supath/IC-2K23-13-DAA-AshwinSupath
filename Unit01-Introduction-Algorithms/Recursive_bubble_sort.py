def b_sort(arr,n,i):
    if n==0:
        return -1
    if i==n-1:
        b_sort(arr,n-1,0)
        return
    if arr[i]<arr[i+1]:
        pass
    else:
        arr[i],arr[i+1]=arr[i+1],arr[i]
    b_sort(arr,n,i+1)
    return arr
    
arr1=[26, 30, 12, 14, 60, 55]
l=b_sort(arr1,len(arr1),0)
print(l)