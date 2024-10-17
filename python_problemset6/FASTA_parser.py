#!/usr/bin/env python3

print(f'FASTA filepath:')
file_input = input()
fastaDict = {}
with open(file_input, "r") as read_file:
  for line in read_file:
    line = line.rstrip()
    if ">" in line:
      line = line.replace(">","")
      fastaDict[line] = ""
      seq_name = line
      line_partial = ""
    else:
      line_partial += line
      fastaDict[seq_name] = line_partial
    #gene_id,seq = line.split()
    #print(gene_id,seq)
print(fastaDict)