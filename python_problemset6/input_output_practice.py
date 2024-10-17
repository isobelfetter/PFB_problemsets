#!/usr/bin/env python3

with open("Python_06.txt", "r") as practice_file, open("Python_06_uc.txt", "w") as output_file:
    for line in practice_file:
        line = line.rstrip()
        upper_line = line.upper()
        output_file.write(f'{upper_line}\n')
print(f"Wrote 'Python_06_uc.txt'.")
