#!/usr/bin/env python3
import sys
number = int(sys.argv[1])
print(f"The number being tested is {number}.")
print(type(number))
if number > 0:
  print(f"{number} is positive.")
