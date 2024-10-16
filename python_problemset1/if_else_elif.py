#!/usr/bin/env python3
number = 60
if number > 0:
  print("positive")
  if number < 50:
    print("less than 50")
    if number%2 == 0:
      print("it is an even number that is smaller than 50")
  elif number > 50:
    print("greater than 50")
    if number%3 == 0:
      print("it is larger than 50 and divisible by 3")
  else:
    print("number is 50")
elif number < 0:
  print("negative")
else:
  print("zero")
