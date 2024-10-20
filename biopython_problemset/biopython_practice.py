#!/usr/bin/env python3
from Bio import SeqIO
import sys

filename = sys.argv[1]
for record in SeqIO.parse(filename, "fasta"):
  print(f'ID\t{record.id}\tSequence length\t{len(record)}')