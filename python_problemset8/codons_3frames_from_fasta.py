#!/usr/bin/env python3

import re
import sys

class NotFASTAError(Exception):
  pass

class NotBaseError(Exception):
  pass

try:
  file_input = sys.argv[1]
  print("User provided file name:", file_input)
  if not file_input.endswith(('.fa', '.fasta', '.nt')):
    raise NotFASTAError("Not a FASTA file")
  fastaDict = {}
  with open(file_input, "r") as read_file:
    for line in read_file:
      line = line.rstrip()
      if re.search(r"(^>(\S+)\s+(.*))", line):
        found = re.search(r"(^>(\S+)\s+(.*))", line)
        gene_name = found.group(2)
        gene_name = re.sub(r">", r"", gene_name)
        fastaDict[gene_name] = ""
        line_partial = ""
      else:
        line_partial += line
        codons = re.findall('[A-Z]{3}', line_partial)
        fastaDict[gene_name] = line_partial
        codon_dict = {}
        if re.search("[^AGTCN]", line_partial):
          raise NotBaseError("Non-nucleotides present in sequence")
    for gene in fastaDict:
        codon_dict[gene] = {}
        codons1 = re.findall('[A-Z]{3}', line_partial)
        codons2 = re.findall('[A-Z]{3}', line_partial[1:])
        codons3 = re.findall('[A-Z]{3}', line_partial[2:])
        codon_dict[gene]['frame-1-codons'] = codons1
        codon_dict[gene]['frame-2-codons'] = codons2
        codon_dict[gene]['frame-3-codons'] = codons3


    write_file = open('Python_08.codons-3frames.nt', 'w')  
    for gene in codon_dict:
      for frame in codon_dict[gene]:  
        write_file.write(f'{gene}-{frame}\n{codon_dict[gene][frame]}\n')
    write_file.close()
  print(f'File written.')

except IndexError:
  print('Error: Please provide a file name')
except IOError:    
  print("Error: Can't find file:" , file_input)
except NotFASTAError:
  print("Error: File needs to be a FASTA file and end with .fa, .fasta, or .nt")
except NotBaseError:
  print("Error: Non-nucleotides present in sequence")
