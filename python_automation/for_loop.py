list_1 = ['Bengaluru', 'Delhi', 'Hyderabad']

for city in list_1:
  print city
  
for letters in 'python':
  print letters
  
for x in xrange(5,8):
  print x    #please note that 8 is not included here
  
for x in xrange(0, len(list_1)):
  print "city with index %s from list_1 is %s" % (x, list_1[x])
  
#sum of first N numbers
n = 10
sum = 0
for i in xrange(1,n+1):
  sum = sum + i
print "Sum is: ", sum

#program to print odd numbers and close program if number 5 appears
for i in range(1,10):
  if(i % 2 == 0):
    continue  #This statement ignores below code and move to next iteration
  elif(i == 5):
    break    #This statement exits the for loop
  else:
    print i
  
