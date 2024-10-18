#!/usr/bin/env python3

import re

print(f'FASTA filepath:')
file_input = input()
fastaDict = {}
nt_count = {}
with open(file_input, "r") as read_file:
  for line in read_file:
    line = line.rstrip()
    if re.search(r"(^>(\S+)\s+(.*))", line):
      found = re.search(r"(^>(\S+)\s+(.*))", line)
      gene_name = found.group(2)
      gene_name = re.sub(r">", r"", gene_name)
      fastaDict[gene_name] = {}
      line_partial = ""
      nt_count = {}
    else:
      line_partial += line
      for nt in line_partial:
        if nt in nt_count:
          nt_count[nt] += 1
        else:
          nt_count[nt] = 1
      fastaDict[gene_name] = nt_count

for fasta in fastaDict:
  print(f'{fasta}\t{fastaDict[fasta]["A"]}\t{fastaDict[fasta]["T"]}\t{fastaDict[fasta]["G"]}\t{fastaDict[fasta]["C"]}')