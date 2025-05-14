# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
print(myint)
print(mystr)
print(mybool)

# Operators are used to perform operations on variables
print(myint + 5)
print(myfloat * 3.6)
print(myint % 3)
print(mystr, "fool!")

another_str = " and this is another string"
print(mystr + another_str)
print("nom " * 3)

# Logical and comparison operators 
print(myint == 10)
print(myint != 10)
print(myint < 4)
print(myfloat / 4 > 10.0)
print(myint < 4 and myfloat > 4.0)
print(myint < 4 or myfloat > 4.0)
print(not(myint < 4 or myfloat > 4.0))

# re-declaring a variable works
# this is bad form however ...

