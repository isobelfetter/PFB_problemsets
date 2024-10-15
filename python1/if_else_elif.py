#!/usr/bin/env python3
number = 18
if number > 0:
  print("positive")
  if number < 50:
    print("less than 50")
    if number%2 == 0:
      print("it is an even number that is smaller than 50")
elif number < 0:
  print("negative")
elif number == 0:
  print("zero")
