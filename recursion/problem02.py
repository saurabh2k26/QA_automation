def b_search(arr, l, r, x):
    if(l is None):
      l=0
    if(r is None):
      r=len(arr)-1
    if(r>=l):
        mid=int((r-l)/2 + l)
        if(arr[mid]==x):
            return mid
        elif(arr[mid]>x):
            return b_search(arr, l, mid-1, x)
        else:
            return b_search(arr, mid+1, r, x)
    else:
        return -1


print b_search([2, 3, 4, 10, 40], None, None, 10)
print b_search([2, 3, 4, 10, 40], None, None, 2)
print b_search([2, 3, 4, 10, 40], None, None, 40)
print b_search([2, 3, 4, 10, 40], None, None, 5)
