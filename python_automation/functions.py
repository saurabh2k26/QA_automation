def func_with_no_argument():
  print "I have no arguments\n"
  
def func_with_two_arguments(a1,a2):
  print "I have 2 arguments ie %s and %s\n" % (a1,a2)
  
def func_with_flexible_no_of_arguments(*a):
  print "I will take any number of arguments passed to me"
  a1, a2, a3 = a
  print "I have 3 arguments ie %s, %s and %s\n" % (a1,a2,a3)
  
#calling functions
func_with_no_argument()
func_with_two_arguments('Sachin','Rahul')
func_with_flexible_no_of_arguments('20','30','40')
