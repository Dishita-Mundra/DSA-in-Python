import array as a

from array import *
val=array('i',[1,2,3,4,5,6,7,8,9])
# val=array('d',[1,2,3,4,5,6,7,8,9.5]) # double type array
# val=array('u',['a','b','c','d','e']) # unicode character array

print(val)

for i in range(0,6): # index 0 included and 6 excluded
    print(val[i] )  # each element on a separate line

for i in range(0,6):
     print(val[i] , end=" ") # all elements on the same line separated by a space

for i in range(0,len(val)): # elements from index 0 to the last index
     print(val[i] , end=" ")

print('\n') # new line
for x in val:
     print(x , end=" , ") 

print('\n')
print(val.typecode) # type of array elements

val.reverse() 
for i in range(0,len(val)): 
     print(val[i] , end=" ")

val.insert(1,50) # insert 50 at index 1
val.append(100) # add 100 at the end of the array
for i in range(0,len(val)):
     print(val[i] , end=" ")
