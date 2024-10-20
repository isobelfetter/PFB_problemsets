#!/usr/bin/env python3
from Bio import SeqIO
import sys

filename = sys.argv[1]
seq_num = 0
total_length = 0
short_seq = 1000000000000
long_seq = 0
total_G = 0
total_C = 0
low_GC = 10000000
high_GC = 0
for record in SeqIO.parse(filename, "fasta"):
  seq_num += 1
  total_length += len(record)
  if len(record) < short_seq:
    short_seq = len(record)
  if len(record) > long_seq:
    long_seq = len(record)
  G_count = record.count('G')
  total_G += G_count
  C_count = record.count('C')
  total_C += C_count
  GC_cont = (G_count + C_count) / len(record)
  if GC_cont < low_GC:
    low_GC = GC_cont
  if GC_cont > high_GC:
    high_GC = GC_cont

total_GC = total_G + total_C
avg_GC = total_GC / total_length
avg_len = total_length / seq_num

  
print(f'sequence count: {seq_num}')
print(f'total number of nucleotides: {total_length}')
print(f'avg len: {avg_len:.1f}')
print(f'shortest len: {short_seq}')
print(f'longest len: {long_seq}')
print(f'avg GC content: {avg_GC:.2%}')
print(f'lowest GC content: {low_GC:.2%}')
print(f'highest GC content: {high_GC:.2%}')