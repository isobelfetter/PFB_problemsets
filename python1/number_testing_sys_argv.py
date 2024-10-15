#!/usr/bin/env python3
import sys
number = int(sys.argv[1])
print(f"The number being tested is {number}.")
if number > 0:
  print(f"{number} is positive.")
  if number < 50:
    print(f"{number} is less than 50.")
    if number%2 == 0:
      print(f"{number} is an even number that is smaller than 50.")
  elif number > 50:
    print(f"{number} is greater than 50.")
    if number%3 == 0:
      print(f"{number} is larger than 50 and divisible by 3.")
  else:
    print(f"{number} is fifty.")
elif number < 0:
  print(f"{number} is negative.")
else:
  print(f"{number} is zero.")
