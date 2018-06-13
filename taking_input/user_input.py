from sys import argv

script_name, param1, param2 = argv

print "name of my script is:", script_name
print "2 variables passed to scripts are:", param1, param2

print "type of param1 is: ",type(param1)

param3 = raw_input("Enter 3rd number: ")
print "variable taken from user is:", param3
print "type of param1 is: ",type(param3)

print "Sum of all 3 variables: ", int(param1) + int(param2) + int(param3)

#output
#$ python user_input.py 1 2
#name of my script is: user_input.py
#2 variables passed to scripts are: 1 2
#<type 'str'>
#Enter 3rd number: 3
#variable taken from user is: 3
#<type 'str'>
#Sum of all 3 variables:  6
