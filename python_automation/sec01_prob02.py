def max_product(arr):
  max = 0
  for i in range(0,len(arr)-1):
    product = arr[i] * arr[i+1]
    if(product > max):
      max = product
  print max
  
max_product([1,2,3,4])
max_product([4,2,3,1])
max_product([100,1,49,2,50,1])
