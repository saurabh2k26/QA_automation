def count(n):
    if(n<0):
        return 0
    elif(n==0):
        return 1
    else:
        return count(n-1)+count(n-2)+count(n-3)
    
print count(3)
print count(4)
print count(5)
