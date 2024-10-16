#!/usr/bin/env python3
import sys
x = int(sys.argv[1])
print(f"The number being tested is {x}.")
if x > 0:
  print(f"{x} is positive.")
  if x < 50:
    print(f"{x} is less than 50.")
    if x%2 == 0:
      print(f"{x} is an even number that is smaller than 50.")
  elif x > 50:
    print(f"{x} is greater than 50.")
    if x%3 == 0:
      print(f"{x} is larger than 50 and divisible by 3.")
  else:
    print(f"{x} is fifty.")
elif x < 0:
  print(f"{x} is negative.")
else:
  print(f"{x} is zero.")
