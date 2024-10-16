#!/usr/bin/env python3

count = 1
factorial = 1
while count <= 1000:
  print(f'{count}! = {factorial}')
  factorial = factorial*(count+1)
  count+=1
print("Done")
