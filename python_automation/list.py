list_1 = ['Bengaluru' , 'Delhi' , 'Pune', 'Hyderabad']
list_2 = [34 , 45 , 12 , 33]

print list_1

print list_1[0]    #print first index of list. Index starts from 0
print list_1[2:]   #print list from index 2 to end
print list_1[1:3]    #print list from index 1 to index(3-1) ie Index 2
print list_1[-2]     #counts index from right starting from -1

print list_2
list_2[1] = 54    #repalce index 1 of list
print list_2

del list_2[0]    #delete index 0
print list_2

list_2.append(100)    # add an item toend of string
print list_2

print len(list_2)    #gives count of items in list

print max(list_2)    #gives maximum from list

print min(list_2)    #gives minimum from list

list_3 = list_1 + list_2   #adding 2 lists
print list_3

print list_2.count(33)    #ives count of object in list

list_2.sort()    #sorts a list
print list_2

list_2.reverse()    #reverse a list
print list_2
