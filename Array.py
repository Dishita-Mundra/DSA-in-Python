# import array as a

# from array import *
# val=array('i',[1,2,3,4,5,6,7,8,9])
# val=array('d',[1,2,3,4,5,6,7,8,9.5]) # double type array
# val=array('u',['a','b','c','d','e']) # unicode character array

# print(val)

# for i in range(0,6): # index 0 included and 6 excluded
#     print(val[i] )  # each element on a separate line

# for i in range(0,6):
#      print(val[i] , end=" ") # all elements on the same line separated by a space

# for i in range(0,len(val)): # elements from index 0 to the last index
#      print(val[i] , end=" ")

# print('\n') # new line
# for x in val:
#      print(x , end=" , ") 

# print('\n')
# print(val.typecode) # type of array elements

# val.reverse() 
# for i in range(0,len(val)): 
#      print(val[i] , end=" ")

# val.insert(1,50) # insert 50 at index 1
# val.append(100) # add 100 at the end of the array
# val[2]=200 # change the value at index 2 to 200
# for i in range(0,len(val)):
#      print(val[i] , end=" ")

##COPY ARRAY
# copyArray=array(val.typecode, (x for x in val)) # create a copy of the array
# copyArray=array(val.typecode, (x*3 for x in val)) # create a copy of the array with each element multiplied by 3

# copyArray.pop(3) # remove the element at index 3
# copyArray.pop() # remove the last element of the array  

# copyArray.remove(15) # remove the first occurrence of 15 from the array

# for i in range(0,len(copyArray)):
#      print(copyArray[i] , end=" ")


##SLICING ARRAY
# abc=val[2:5] # create a new array with elements from index 2 to 4
# abc=val[2:-3] # create a new array with elements from index 2 to the third last index
# abc=val[::-1] # create a new array with elements in reverse order
# for i in range(0,len(abc)):
#      print(abc[i] , end=" ")


##ARRAY OF USER INPUT
# arr=array('i', []) # create an empty array of integers
# n=int(input("Enter number of elements:"))
# for i in range (0,n): 
#     arr.append(int(input("Enter element:"))) # add elements to the array
# for x in arr:
#     print(x,end=" ")


# arr=array('i',[12,23,45,234,134,235])
# i=arr.index(45) # find the index of the first occurrence of 45
# print(i)


##ARRAY USING NUMPY
from numpy import *
# val=array([1,2,4.5,'a']) # create a numpy array
# val=array([1,2,4],float) 

# val=linspace(10,20,11) # create an array of 11 equally spaced values between 10 and 20
# val=arange(10,20,2) # create an array of values from 10 to 20 with a step of 2 and 20 is not included
# val=logspace(10,20,2) # create an array of 2 values between 10^10 and 10^20
# val=zeros(10) # create an array of 10 zeros
# val=ones(10) # create an array of 10 ones
# val=full(10,5) # create an array of 10 elements with the value 5
# for x in val:
#     print(x,end=" ") # print each element of the array on the same line separated by a space

# for x in val:
#     print(x) # print each element of the array on a separate line


## Dimensional array
# zero=array(10) 
# print(zero)

# one=array([1,2,3,4,5])
# print(one)

# two=array([[1,2,3],[4,5,6],[7,8,9]])
# print(two)

three=array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(three)
