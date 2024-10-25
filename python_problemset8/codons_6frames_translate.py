#!/usr/bin/env python3

import re, sys

file_input = sys.argv[1]
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

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

peptide_dict = {}
longest_peptide = ""
long_peptide_dict = {}
for gene in codon_dict:
  peptide_dict[gene] = {}
  for frame in codon_dict[gene]:
    codon_list = codon_dict[gene][frame]
    amino_acid_list = [translation_table.get(codon) for codon in codon_list]
    peptide = "".join(amino_acid_list)
    peptide_dict[gene][frame] = peptide
    if re.search(r'(M\w*\*)', peptide):
      found = re.search(r'(M\w*\*)', peptide)
      long_peptide = found.group(1)
      long_peptide_dict[f'{gene}-{frame}'] = long_peptide
    
print(long_peptide_dict)

write_file1 = open('Python_08.codons-6frames.nt', 'w')  
for gene in codon_dict:
  for frame in codon_dict[gene]:  
    write_file1.write(f'{gene}-{frame}\n{codon_dict[gene][frame]}\n')
write_file1.close()


write_file2 = open('Python_08.translated.aa', 'w')  
for gene in peptide_dict:
  for frame in peptide_dict[gene]:  
    write_file2.write(f'{gene}-{frame}\n{peptide_dict[gene][frame]}\n')
write_file2.close()
print(f'File written.')

# write_file3 = open('Python_08.translated-longest.aa', 'w')
# for gene in long_peptide_dict:
#   write_file3.write(f'{gene}\n{long_peptide_dict[gene]}\n')

#longest needs to be more fleshed out, make dictionary of longest read, then sort by length and print first item for each gene