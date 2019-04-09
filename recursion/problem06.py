def single_sum(n):
    if(n<10):
        return n
    else:
        t=0
        for i in str(n):
            t=t+int(i)
        return single_sum(t)
            

    
print single_sum(12345)
print single_sum(2222)
print single_sum(12341234123412341234)
