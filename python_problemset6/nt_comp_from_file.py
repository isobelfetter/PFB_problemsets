#!/usr/bin/env python3

seq_dict = {}
nt_counts = {}

with open("Python_06.seq.txt", 'r') as sequences:
  for line in sequences:
    line = line.rstrip()
    gene_id,seq = line.split()
    seq_dict[gene_id] = seq


with open("Python_06.seq_nt_counts.txt", "w") as output_file:
  output_file.write(f'Name\tA\tT\tG\tC\tGC content\n')
  for gene in seq_dict:
    seq = seq_dict[gene]
    for nt in seq:
      nt_counts = {"A":0, "T":0, "G":0, "C":0}
      count = seq.count(nt)
      nt_counts[nt] = count
      GC_count = int(nt_counts["G"]) + int(nt_counts["C"])
      total_length = len(seq)
      GC_content = GC_count / total_length
    output_file.write(f'{gene}\t{nt_counts["A"]}\t{nt_counts["T"]}\t{nt_counts["G"]}\t{nt_counts["C"]}\t{GC_content:.1%}\n')
print("File written")