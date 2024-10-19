#!/usr/bin/env python3

class DNASequence(object):
    def __init__(self, sequence, gene_name, species_name):
      self.sequence = sequence
      self.gene_name = gene_name
      self.species_name = species_name
      #self.A = nt_dict["A"]

    def len(self):
       length = len(self.sequence)
       return length
    
    def comp(self):
       nt_dict = {}
       for nt in self.sequence:
          if nt not in nt_dict:
             nt_dict[nt] = 1
          else:
             nt_dict[nt] += 1
       return nt_dict 
    
    def GC_cont(self):
       nt_dict = {}
       for nt in self.sequence:
          if nt not in nt_dict:
             nt_dict[nt] = 1
          else:
             nt_dict[nt] += 1
       GC_count = int(nt_dict['C']) + int(nt_dict['G'])
       length = len(self.sequence)
       GC_content = GC_count / length
       return f'{GC_content:.2%}'
    
    def AT_cont(self):
       nt_dict = {}
       for nt in self.sequence:
          if nt not in nt_dict:
             nt_dict[nt] = 1
          else:
             nt_dict[nt] += 1
       AT_count = int(nt_dict['A']) + int(nt_dict['T'])
       length = len(self.sequence)
       AT_content = AT_count / length
       return f'{AT_content:.2%}'
    
    def fasta(self):
       return f'>{self.gene_name} {self.species_name}\n{self.sequence}'

seq1 = DNASequence('ATGCATGCAATAAAAAAATGC', 'ROBO4', 'Homo sapiens')
print(seq1.sequence, seq1.gene_name, seq1.species_name) #attributes don't need ()
print(seq1.len()) #methods do need ()
print(seq1.comp())
print(seq1.GC_cont())
print(seq1.AT_cont())
print(seq1.fasta())