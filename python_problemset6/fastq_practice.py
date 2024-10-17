#!/usr/bin/env python3

line_count = 0
total_char = 0
with open("Python_06.fastq", "r") as read_file:
  for line in read_file:
    line = line.rstrip()
    char_count = len(line)
    line_count += 1
    total_char += char_count
avg_char = total_char / line_count
print(f'Total lines: {line_count}\nTotal characters:{total_char}\nAverage line length:{avg_char}')