print 'hi'

print "hi"

print 'I"m tester'

print "I'm tester"

print "I\"m tester"

hobby = 'coding'
number = 6
print "my hobby is", hobby
print "my hobby is " + hobby
print "my hobby is %s" %hobby
print "my hobby is " + hobby + " and my lucky number is " + str(number)
print "my hobby is %s and my lucky number is %s" % (hobby, number)
print "my hobby is %s and my lucky number is %d" % (hobby, number)
# below line would generate error since %d is used for numbers, not string
# print "my hobby is %d and my lucky number is %d" % (hobby, number)

print 'what is 4 + 7:', 4 + 7

print 1 + 2 < 4
print 1 + 2 > 4

print "s" * 5

#multiline print
print "line1\nline2"
print """line1
line2
"""

#output
#hi
#hi
#I"m tester
#I'm tester
#I"m tester
#my hobby is coding
#my hobby is coding
#my hobby is coding
#my hobby is coding and my lucky number is 6
#my hobby is coding and my lucky number is 6
#my hobby is coding and my lucky number is 6
#what is 4 + 7: 11
#True
#False
#sssss
#line1
#line2
#line1
#line2
