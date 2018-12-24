def find_sum(num):
  if(num==0):
    print num
  elif(num % 9 == 0):
    print 9
  else:
    print num % 9
    
find_sum(36934)   # ie 3+6+9+3+4 = 25 = 2+5 = 7
find_sum(9999)
find_sum(1111) 
find_sum(2008)
