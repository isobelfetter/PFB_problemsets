#!/usr/bin/env python3

import re

print(f'FASTA filepath:')
file_input = input()
fastaDict = {}
with open(file_input, "r") as read_file, open('Python_08.codons-frame-1.nt', 'w') as write_file:
  for line in read_file:
    line = line.rstrip()
    if re.search(r"(^>(\S+)\s+(.*))", line):
      found = re.search(r"(^>(\S+)\s+(.*))", line)
      gene_name = found.group(2)
      gene_name = re.sub(r">", r"", gene_name)
      fastaDict[gene_name] = []
      line_partial = ""
    else:
      line_partial += line
      codons = re.findall('[A-Z]{3}', line_partial)
      fastaDict[gene_name] = codons
    write_file.write(f'{gene_name}-frame-1-codons\n{fastaDict[gene_name]}\n')
print(f'File written.')