#!/usr/bin/env python3

with open("Python_06.seq.txt", "r") as read_file, open("reverse_complement.txt", "w") as write_file:
  for line in read_file:
    line = line.rstrip()
    gene_id,seq = line.split()
    complement = "".join(rc_dict.get(nt) for nt in seq)
    rev_comp = complement[::-1]
    write_file.write(f'>{gene_id}_reverse_comp\t{rev_comp}\n')
print(f'File Written')