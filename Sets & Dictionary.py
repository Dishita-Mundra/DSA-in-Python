# set1 = {2,4,"hello",2,"dishita","hello",2,4}

# print(set1)
# print(type(set1))
# print(len(set1))



# l1=[3,4,6,3,2,4,56,7,5,2,2,4,6,23,2,45,5]

# count number of unique elements in this list
# set1 = set(l1)
# print(len(set1))
# print(set1)



# set1 = {'hello',2,4,'dishita'}

# set1.add(100)
# set1.add("hello")

# set1.discard("hello")
# set1.discard("hii")

# set1.remove(2)
# set1.remove("hii")   # ERROR

# print(set1)



# set1 = {'hello',2,4,'dishita'}

# if "hello" in set1:
#     print(True)
# else:
#     print(False)

# if "hii" in set1:
#     print(True)
# else:
#     print(False)


# set1.clear()
# print(set1)



# set1 = {1,2,3}
# set2 = set1  # DEEP COPY

# set2 = set1.copy()  # SHALLOW COPY

# set2.add(4)

# print(set1)
# print(set2)



set1 = {1,8,5,2,4}
set2 = {8,2,9,6}

# union
print(set1|set2)
print(set1.union(set2))

# intersection
print(set1&set2)
print(set1.intersection(set2))

# difference
print(set1-set2)
print(set1.difference(set2))

print(set2-set1)
print(set2.difference(set1))

# symmetric difference = union-intersection
print(set1^set2)
print(set1.symmetric_difference(set2))