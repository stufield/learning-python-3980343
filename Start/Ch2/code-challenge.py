
def count_numbers(which, numbers):
  if which != "even" and which != "odd":
    return -1
  count = 0
  int = 0 if which == "even" else 1
  for i in numbers:
    if (i % 2 == int):
      count += 1
  return count

numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

even = count_numbers("even", numbers)
odd  = count_numbers("odd", numbers)
bad  = count_numbers("foo", numbers)

print("Even count:", even)
print("Odd count:", odd)
print("Incorrect 'which' parameter count:", bad)
