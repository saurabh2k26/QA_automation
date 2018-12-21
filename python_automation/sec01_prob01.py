def reverse_method_1(num):
    x = num
    reverse= 0
    while num:
        reverse= reverse*10 + num%10
        num = num//10
    print "reverse of %s is %s" % (x, reverse)
    
def reverse_method_2(num):
  reverse = str(num)[::-1]
  reverse = int(reverse)
  print "reverse of %s is %s" % (num, reverse)
    
reverse_method_1(1)
reverse_method_1(721)
reverse_method_1(13531)

reverse_method_2(1)
reverse_method_2(721)
reverse_method_2(13531)
    
