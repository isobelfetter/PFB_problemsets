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

contig_dict = {}
for contig in fastaDict:
  found = re.search(r'^(tig\d+) len=(\d+)', contig)
  contig_name = found.group(1)
  contig_len = found.group(2)
  contig_dict[contig_name] = int(contig_len)

sorted_dict = sorted(contig_dict, key=contig_dict.get)
reverse_sorted_dict = sorted(contig_dict, key=contig_dict.get, reverse=True)

total_len = 0
for contig in contig_dict:
  total_len += contig_dict[contig]

N50_sum = 0
L50 = 0

for contig_name in reverse_sorted_dict:
  N50_sum += contig_dict[contig_name]
  L50 += 1
  if N50_sum > total_len / 2:
    N50 = contig_dict[contig_name]
    break
  

print(f'Number of contigs: {len(fastaDict)}')
print(f'Shortest contig: {sorted_dict[0]}')
print(f'Longest contig: {reverse_sorted_dict[0]}')
print(f'Total contig length: {total_len}')
print(f'N50:{N50}')
print(f'L50:{L50}')