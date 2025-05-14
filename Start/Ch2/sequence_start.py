# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]
print(len(mylist))
print(mylist[2])
print(mylist[-1])
mylist[0] = 10

# to access a member of a sequence type, use []
print(mylist)

# add a list to another list
another_list = [6,7,8]
mylist2 = mylist + another_list
print(mylist2)

mystr = "This is a string"
print(mystr[2])

#mystr[2] = "I"    # You cannot assign elements with `[` for string class

# use slices to get parts of a sequence
print(mylist[1:4])
print(mylist[1:4:2])   # use a by= argument

# you can use slices to reverse a sequence
print(mylist[::-1])   # same as rev()
print(mylist[3::-1])   # same as rev()

# Tuples are like lists, but they are immutable
mytuple = (0, 1, 2, "three")
print(mytuple[1])

# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 2, 4, "hey"}   # forced uniqueness
print(myset)   # second '2' is dropped

# Set, however, can not be indexed like lists or tuples

# print(myset[0]) # this will cause an error

# Test for membership
print(1 in mylist)
print(3 in mytuple)
print(5 in myset)

