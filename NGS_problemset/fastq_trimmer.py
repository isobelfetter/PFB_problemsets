#!/usr/bin/env python3

import sys, re

file_input = sys.argv[1]
#quality_score = sys.argv[2]

new_file = re.sub(r'.fastq', r'.trim.fastq', file_input)

line_count = 0
with open(file_input, 'r') as read_file, open(new_file, 'w') as write_file:
    for line in read_file:
        stripped_line = line.rstrip()
        line_count += 1
        if line_count % 4 == 1:
            name = stripped_line
        if line_count % 4 == 2:
            sequence = stripped_line
        if line_count % 4 == 3:
            plus = stripped_line
        if line_count % 4 == 0:
            score = stripped_line
            write_file.write(f'{name}\n{sequence}\n{plus}\n{score}\n')


print(f'fastq file trimmed')