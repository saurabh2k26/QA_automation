def feb(n,k):
    if(k is None):
      k=n
    if(k==0):
        return
    if(n%k==0):
        print k
    return feb(n,k-1)

print feb(180, None)
