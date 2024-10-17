#!/usr/bin/env python3

dna = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in dna:
  length = len(seq)
  index = dna.index(seq)
  print(f'{index}\t{length}\t{seq}')
