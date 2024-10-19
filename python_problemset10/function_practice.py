#!/usr/bin/env python3

import re
import sys

def DNA_nt_length(file_input = "", width = 60):
    file_input = sys.argv[1]
    width = sys.argv[2]
    fastaDict = {}
    with open(file_input, 'r') as read_file:
      for line in read_file:
        line = line.rstrip()
        if re.search(r"(^>(\S+)\s+(.*))", line):
          found = re.search(r"(^(>\S+)\s+(.*))", line)
          gene_name = found.group(2)
          #gene_name = re.sub(r">", r"", gene_name)
          fastaDict[gene_name] = ""
          line_partial = ""
        else:
          line_partial += line
          concat_line = re.sub(r'\s', r'', line_partial)
          pattern = '([ATGCN]{'+str(width)+'})'
          split_lines = re.sub(pattern, r'\1\n', concat_line)
          fastaDict[gene_name] = split_lines
    for gene in fastaDict:
      #print(f'{gene}\n{fastaDict[gene]}') #prints all but nothing returned?
      return f'{gene}\n{fastaDict[gene]}' #will only print first item in dict
      


print(DNA_nt_length())
