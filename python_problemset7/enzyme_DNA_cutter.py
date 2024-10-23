#!/usr/bin/env python3

import re, sys
line_count = 0
enzyme_dict = {}

with open('enzyme_list.txt', 'r') as read_file:
    for line in read_file:
        line_count += 1
        if line_count > 10:
            line = line.rstrip()
            found = re.search(r'^(\S+).*?(\S+)$', line)
            enzyme = found.group(1)
            cut_site = found.group(2)
            if '^' in cut_site:
                enzyme_dict[enzyme] = cut_site

fasta_file = sys.argv[1]
enzyme = sys.argv[2]

fastaDict = {}
with open(fasta_file, "r") as read_file:
  for line in read_file:
    line = line.rstrip()
    line_partial = ""
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

pattern = enzyme_dict[enzyme]
degen_dict = {"W":"[AT]", "S":"[CT]", "M":"[AC]", "K":"[GT]", "R":"[AG]", "Y":"[CT]", "B":"[CGT]", "D":"[AGT]", "H":"[ACT]", "V":"[ACG]", "N":"[ACGT]"}
for degen in degen_dict:
  if degen in pattern:
    pattern = pattern.replace(degen, degen_dict[degen])

pattern_no_cut = re.sub(r'\^', '', pattern)   

for seq_name in fastaDict:
    sequence = fastaDict[seq_name]
    if re.search(pattern_no_cut, sequence):
        cut_sequence = re.sub(pattern_no_cut, pattern, sequence) #need to figure out how to go back to original sequence instead of subbing in degens

print(cut_sequence)
fragments = cut_sequence.split('^')
print(f'Number of fragments: {len(fragments)}')
print(fragments)
sorted_fragments = sorted(fragments, key = len, reverse=True)
for fragment in sorted_fragments:
  print(fragment)
