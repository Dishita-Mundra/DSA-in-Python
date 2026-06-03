### LIST

# names = ["dishi","swati","aarti","anu"]

# print(names,type(names))
# print(type(names))
# print(len(names))

# names[0] = "dishita"

# print(names[0])
# print(names[2])
# print(names[-1])

# list1 = [5,"hello",34.23,True,214]
# print(list1)

# list1 = [4,2,1,7,8,4]
# list1.append(9)
# list1.append([1,2,3,])
# list1.extend([1,2,3,])

# print(list1)


# list1 = [32,6,2,42,35,12]
# list1.insert(3,100)

# print(list1) 


# list1 = [32,6,2,42,35,12]
# list1.remove(42)    # remove a given element
# list1.pop()    # by default remove last element
# list1.pop(1)   # remove element at index 1

# print(list1)

# list1.clear()
# print(list1)


# list1 = [32,6,2,42,35,12]
# print(min(list1))  # O(n)
# print(max(list1))  # O(n)


# list1 = [4,1,2,5,3,2,1,3,2,4,5,3,2,1,2]

# print(list1.count(1))
# print(list1.count(2))
# print(list1.count(3))
# print(list1.count(4))
# print(list1.count(5))

# list1.sort()   # O(nlogn)
# print(list1)

# list1.reverse()   # O(n)
# print(list1)


# list1 = [1,5,3,2,5,7,3]

# print(list1.index(2))
# print(list1.index(5))
# print(list1.index(5,2))



# l1 = [1,2,3,]
# l2 = l1       # DEEP COPY

# l2.append(4)

# print(l1)
# print(l2)



# l1 = [1,2,3,]
# l2 = l1.copy()     # SHALLOW COPY

# l2.append(4)

# print(l1 , id(l1))
# print(l2 , id(l2))



# l1 = [3,4,456,24,312,234,456,42,23]

# print(l1[2:6])
# print(l1[2:8:3])
# print(l1[8:1:-2])
# print(l1[:5])
# print(l1[:])

# print(l1[::-1])





### TUPLE

# t1 = ("hello",123,23.232,True,324.423)
# print(t1)
# print(t1[3])
# print(t1[-5])

# t1=(1,2,3)
# t2=t1

# print(t1,id(t1))
# print(t2,id(t2))

# t1=(3,4,456,24,312,234,456,42,23)

# print(t1[2:4])
# print(t1.count(456))
# print(t1.index(456))

# t1=(3,4,456,24,312,234,456,42,23)
# l1=list(t1)
# print(l1)





### STRING

# name= "Dishita"
# print(name,type(name))

name="Physics wallah Skills"

print(name[4])
print(name[-2])
print(len(name))
print(name.lower())
print(name.upper())
print(name.capitalize())
