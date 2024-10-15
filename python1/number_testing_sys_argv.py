#!/usr/bin/env python3
import sys
number = int(sys.argv[1])
print(f"The number being tested is {number}.")
if number > 0:
  print(f"{number} is positive.")
  if number < 50:
    print(f"{number} is less than 50.")
    if number%2 == 0:
      print(f"{number} is even.")
elif number < 0:
  print(f"{number} is negative.")
else:
  print(f"{number} is zero.")
