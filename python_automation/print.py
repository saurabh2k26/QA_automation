#print using single quotes
print 'hi'

#print using double quotes
print "hi"  

#print double quote
print 'I"m tester'

#print single quote
print "I'm tester"

#print double quote using backslash
print "I\"m tester"

hobby = 'coding'
number = 6

#print variable using comma
print "my hobby is", hobby

#print variable using plus symbol
print "my hobby is " + hobby

#print variable using ampersand
print "my hobby is %s" %hobby

#using multiple variables
print "my hobby is " + hobby + " and my lucky number is " + str(number)
print "my hobby is %s and my lucky number is %s" % (hobby, number)
print "my hobby is %s and my lucky number is %d" % (hobby, number)

# below line would generate error since %d is used for numbers, not string
# print "my hobby is %d and my lucky number is %d" % (hobby, number)

#arithematic operation in print statement
print 'what is 4 + 7:', 4 + 7

#boolean operation in print statement
print 1 + 2 < 4
print 1 + 2 > 4

#multiply operation with string in print statement
print "s" * 5

#multiline print format 1
print "line1\nline2"

#multiline print format 2
print """line1
line2
"""
