#!/usr/bin/env python3
import sys
min_value = int(sys.argv[1])
max_value = int(sys.argv[2])

for num in range(min_value,max_value+1): #for loop
  if num%2 != 0:
    print(num)

odds = [num for num in range(min_value, max_value+1) if num%2 != 0] #list comprehension
print(odds)
