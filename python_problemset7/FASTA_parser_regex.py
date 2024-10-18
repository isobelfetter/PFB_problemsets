#!/usr/bin/env python3

import re

print(f'FASTA filepath:')
file_input = input()
fastaDict = {}
with open(file_input, "r") as read_file:
  for line in read_file:
    line = line.rstrip()
    if re.search(r"(^>(\S+)\s+(.*))", line):
      found = re.search(r"(^>(\S+)\s+(.*))", line)
      header = found.group(1)
      line = re.sub(r">", r"", header)
      print(line)
      fastaDict[line] = ""
      seq_name = line
      line_partial = ""
    else:
      line_partial += line
      fastaDict[seq_name] = line_partial
print(fastaDict)