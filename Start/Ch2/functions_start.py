# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions

# define a basic function
def hello_func():
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)

hello_func()

# function that takes parameters
def hello_func(name):
  print("hello world!")
  print("Nice to meet you,", name)

hello_func("John")

# function that returns a value
def cube(x):
  return x^3

print(cube(5))
print(3^3)

# function with default value for an parameter
def hello_func(greeting, name=None):
  if name == None:
    name = input("What is your name? ")
  print(greeting, name)

hello_func("Nice to meet you")
hello_func("Nice to meet you", "Joe")
hello_func("Nice to meet you")
hello_func(name = "Joe", greeting = "Nice to meet you")

# function with variable number of parameters
def multi_add(start, *params):   # similar to '...' in R
  result = start  
  for p in params:
    result = result + p
  return result

print(multi_add(1, 4, 5, 10, 5))

