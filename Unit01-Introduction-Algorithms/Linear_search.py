def l_s(a):
    lst=[1,2,3,4,5,6,7,8,9,10]
    for i in range(0,len(lst)):
        if lst[i] == a:
            print (lst[i], " is present in the list at index:- \n", i)
            break
        elif lst[i] ==len(lst):
            print("Element not found...!")
            
        else:
            continue

l1=l_s(5)