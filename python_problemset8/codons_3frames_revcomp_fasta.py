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
      gene_name = found.group(2)
      gene_name = re.sub(r">", r"", gene_name)
      fastaDict[gene_name] = ""
      line_partial = ""
    else:
      line_partial += line
      codons = re.findall('[A-Z]{3}', line_partial)
      fastaDict[gene_name] = line_partial
codon_dict = {}
for gene in fastaDict:
  codon_dict[gene] = {}
  codons1 = re.findall('[A-Z]{3}', line_partial)
  codons2 = re.findall('[A-Z]{3}', line_partial[1:]) #loop for iteration? 0-2 for strings, f-string to rename variable/key in dictionary
  codons3 = re.findall('[A-Z]{3}', line_partial[2:])
  complement = re.sub("A", "t", line_partial)
  complement = re.sub("T", "a", complement)
  complement = re.sub('C', 'g', complement)
  complement = re.sub('G', 'c', complement)
  reverse_complement = complement[::-1]
  reverse_complement = reverse_complement.upper()
  rv_codons1 = re.findall('[A-Z]{3}', reverse_complement)
  rv_codons2 = re.findall('[A-Z]{3}', reverse_complement[1:])
  rv_codons3 = re.findall('[A-Z]{3}', reverse_complement[2:])
  codon_dict[gene]['frame-1-codons'] = codons1
  codon_dict[gene]['frame-2-codons'] = codons2
  codon_dict[gene]['frame-3-codons'] = codons3
  codon_dict[gene]['frame-1-codons-rev-comp'] = rv_codons1
  codon_dict[gene]['frame-2-codons-rev-comp'] = rv_codons2
  codon_dict[gene]['frame-3-codons-rev-comp'] = rv_codons3

write_file = open('Python_08.codons-6frames.nt', 'w')  
for gene in codon_dict:
    for frame in codon_dict[gene]:  
      write_file.write(f'{gene}-{frame}\n{codon_dict[gene][frame]}\n')
write_file.close()
print(f'File written.')