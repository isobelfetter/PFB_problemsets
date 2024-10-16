#!/usr/bin/env python3
numbers = [101,2,15,22,95,33,2,27,72,15,52]
for num in numbers:
  if num%2 == 0:
    print(num)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
for num in sorted_numbers:
  print(num)
evens = [num for num in sorted_numbers if num%2 == 0]
print("evens:", evens)
even_sum = 0
for num in evens:
  even_sum = even_sum + num
odds = [num for num in sorted_numbers if num%2 != 0]
print("odds:", odds)
odd_sum = 0
for num in odds:
  odd_sum = odd_sum + num
print(f'Sum of even numbers: {even_sum}\nSum of odds: {odd_sum}')
