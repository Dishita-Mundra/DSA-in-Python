### SETS

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



# set1 = {1,8,5,2,4}
# set2 = {8,2,9,6}

# union
# print(set1|set2)
# print(set1.union(set2))

# intersection
# print(set1&set2)
# print(set1.intersection(set2))

# difference
# print(set1-set2)
# print(set1.difference(set2))

# print(set2-set1)
# print(set2.difference(set1))

# symmetric difference = union-intersection
# print(set1^set2)
# print(set1.symmetric_difference(set2))





### DICTIONARIES

# x = {}

# print(type(x))


# d1 = {1:"dishita" , "hello":100 , 10.21:"hii" , "key":True}

# print(d1)
# print(type(d1))
# print(len(d1))

# d1 = {[1,2,3]:"dishita" , "hello":100 , 10.21:"hii" , "key":True}  # Error as list is mutable
# print(d1)

# d1 = {(1,2,3):"dishita" , "hello":100 , 10.21:"hii" , "key":True}  # Error as list is mutable
# print(d1)


# d1 = {1:"dishita" , "hello":100 , 10.21:"hii" , "key":True}

# print(dict[1])
# print(dict["hello"])
# print(d1)


# d1 = {1:"dishita" , 2:"swati" , 3:"ananya" , 4:"anu"}

# d1[5] = "swati"
# d1[2] = "ani"

# d1.update({1 :"dishi" , 10:"gungun"})

# print(d1)

# d1=dict(dishita=1 , swati=2)
# print(d1)

# d1 = {1:"dishita" , 2:"swati" , 3:"ananya" , 4:"anu"}

# d1.pop(2)
# del d1[1]

# print(d1)


# d1 = {1:"dishita" , 2:"swati" , 3:"ananya" , 4:"anu"}

# print(d1[2])
# print(d1.get(1))


# d1 = {1:"dishita" , 2:"swati" , 3:"ananya" , 4:"anu"}
# d2 = d1.copy()

# d2[10] = "hello"

# print(d1)
# print(d2)

# d1.clear()


# d1 = {1:"dishita" , 2:"swati" , 3:"ananya" , 4:"anu"}

# print(d1.items())
# for key,value in d1.items():
#     print(key,value)

# print(d1.keys())
# for key in d1.keys():
#     print(key)

# print(d1.values())
# for value in d1.values():
#     print(value)