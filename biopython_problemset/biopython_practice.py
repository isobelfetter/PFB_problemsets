#!/usr/bin/env python3
from Bio import SeqIO
import sys

filename = sys.argv[1]
seq_num = 0
total_length = 0
short_seq = 1000000000000
long_seq = 0
for record in SeqIO.parse(filename, "fasta"):
  print(f'ID\t{record.id}\tSequence length\t{len(record)}')
  seq_num += 1
  total_length += len(record)
  if len(record) < short_seq:
    short_seq = len(record)
  if len(record) > long_seq:
    long_seq = len(record)
  
print(f'sequence count: {seq_num}')
print(f'total number of nucleotides: {total_length}')
print(f'avg len: {total_length / seq_num}')
print(f'shortest len: {short_seq}')
print(f'longest len: {long_seq}')