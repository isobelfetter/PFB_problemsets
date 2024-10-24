#!/usr/bin/env python3

import sys, re

file_input = sys.argv[1]

fastaDict = {}
with open(file_input, "r") as read_file:
  for line in read_file:
    line = line.rstrip()
    if re.search(r"(^>(\S+)\s+(.*))", line):
      found = re.search(r"(^>(\S+)\s+(.*))", line)
      header = found.group(1)
      line = re.sub(r">", r"", header)
      fastaDict[line] = ""
      seq_name = line
      line_partial = ""
    else:
      line_partial += line
      fastaDict[seq_name] = line_partial

nt_dict = {}
for contig in fastaDict:
  for nt in fastaDict[contig]:
    if nt not in nt_dict:
      nt_dict[nt] = 1
    else:
      nt_dict[nt] += 1

sorted_nts = sorted(nt_dict)

print(f'Number of contigs: {len(fastaDict)}')
for nt in sorted_nts:
  print(f'{nt}: {nt_dict[nt]}')

total_len = 0
masked_len = 0
for contig in fastaDict:
  for nt in sorted_nts:
    total_len += nt_dict[nt]
    if nt.isupper() != True:
      masked_len += nt_dict[nt]

print(f'Masked Content: {masked_len / total_len:.2%}')