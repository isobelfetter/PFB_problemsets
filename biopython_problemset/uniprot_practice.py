#!/usr/bin/env python3
from Bio import SeqIO
import sys
import re

filename = sys.argv[1]
seq_num = 0
sequence_IDs = []
sequence_desc = []
species_list = []
species_dict = {}
pattern = "OS=(.+?)( [(]| OX=)"
salmon_list = []

for record in SeqIO.parse(filename, "fasta"):
  seq_num += 1
  sequence_IDs.append(record.id)
  sequence_desc.append(record.description)
  found = re.search(pattern, record.description)
  species = found.group(1)
  species_list.append(species)
  if species not in species_dict:
    species_dict[species] = 1
  else:
    species_dict[species] += 1
  if species == "Salmonella paratyphi B":
    salmon_list.append(record)

SeqIO.write(salmon_list, 's_paratyphi.prot.fa', 'fasta')



#print(sequence_IDs)
#print(sequence_desc) #description is everything besides sequence >TP53 tumor protein etc etc etc