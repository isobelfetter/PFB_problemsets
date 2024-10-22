#!/usr/bin/env python3

import re, sys

file_input = sys.argv[1]
fastaDict = {}
line_partial = ""

with open(file_input, 'r') as read_file:
    for line in read_file:
        line = line.rstrip()
        if re.search(r"(^>(\S+))", line):
            found = re.search(r"(^>(\S+))", line)
            header = found.group(1)
            line = re.sub(r">", r"", header)
            fastaDict[line] = ""
            seq_name = line
            line_partial = ""
        else:
            line_partial += line
            fastaDict[seq_name] = line_partial

for seq_name in fastaDict:
    sequence = fastaDict[seq_name]
    for found in re.finditer('([A|G])AATT([C|T])', sequence):
        start = found.start(0) + 1
        end = found.end(0)
        print(f'{start}-{end}')
    cut_sequence = re.sub(r'([A|G])AATT([C|T])', r'\1^AATT\2', sequence)
    print(cut_sequence)
    fragments = cut_sequence.split('^')
    sorted_fragments = sorted(fragments, key=len, reverse=True)
    for fragment in sorted_fragments:
        print(fragment)
