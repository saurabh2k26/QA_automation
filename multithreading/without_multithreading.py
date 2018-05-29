#!/usr/bin/python

import time

a = [5,12,1,3,7,31,6,121,30,123,67,42]

def square(i):
    time.sleep(2)
    return i * i

start_time = time.time()
for i in a:
    print "square of "+str(i)+ " is: "+str(square(i))+"\n"
elapsed_time = time.time() - start_time
print "total time taken is " + str(elapsed_time)

##output:
##square of 5 is: 25
##square of 12 is: 144
##square of 1 is: 1
##square of 3 is: 9
##square of 7 is: 49
##square of 31 is: 961
##square of 6 is: 36
##square of 121 is: 14641
##square of 30 is: 900
##square of 123 is: 15129
##square of 67 is: 4489
##square of 42 is: 1764
##
##total time taken is 25.3074791431
