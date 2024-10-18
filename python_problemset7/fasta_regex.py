#!/usr/bin/env python3

import re

with open("Python_07.fasta", "r") as FASTA_file:
    for line in FASTA_file:
      line = line.rstrip()
      for found in re.finditer(r"(^>(\S+)\s+(.*))", line):
        header = found.group(1)
        seq_name = found.group(2)
        desc = found.group(3)
        print(f'id:{seq_name}\tdesc:{desc}')