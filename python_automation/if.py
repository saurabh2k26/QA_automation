def example_if(num):
  if(num == 0):
    print "number is %s\n" %(num)
    
def example_if_else(num):
  if(num == 0):
    print "number is %s\n" %(num)
  else:
    print "number is not 0\n"
    
def example_multiple_if(num):
  if(num == 0):
    print "number is %s" %(num)
  else:
    print "number is not 0"
  if(num % 2 == 0):
    print "number is even\n"
  else:
    print "number is odd\n"
    
def example_if_elif_else(num):
  if(num == 0):
    print "number is %s\n" %(num)
  elif(num % 2 == 0):
    print "number is even\n"
  else:
    print "number is odd\n"

#calling functions    
example_if(0)   #this will print - number is 0
example_if(1)   #this will not print anything since condition is not met

example_if_else(0)    #this will print - number is 0
example_if_else(1)    #this will print - number is not 0

example_multiple_if(0)
example_multiple_if(1)

example_if_elif_else(0)
example_if_elif_else(1)
example_if_elif_else(2)
