def mult(a,b,s=0):
    res = b + s
    if(a!=1):
        return mult(a-1,b,res)
    return res

print mult(8,7)
print mult(100,200)
