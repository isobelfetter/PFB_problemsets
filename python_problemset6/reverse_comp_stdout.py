#!/usr/bin/env python3

rc_dict = {'A':'T','T':'A','G':'C','C':'G'}
with open("Python_06.seq.txt", "r") as read_file, open("reverse_complement.txt", "w") as write_file: #need to figure out how to get user input
  for line in read_file:
    line = line.rstrip()
    gene_id,seq = line.split()
    complement = "".join(rc_dict.get(nt) for nt in seq)
    rev_comp = complement[::-1]
    print(f'>{gene_id}_reverse_comp\t{rev_comp}\n')
