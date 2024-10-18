#!/usr/bin/env python3

all_set = set()
pigment_set = set()
stem_set = set()
with open("ferret_all_genes.tsv", "r") as all_genes, open('ferret_pigmentation_genes.tsv', "r") as pigment_genes, open('ferret_stemcellproliferation_genes.tsv', 'r') as stem_genes:
  for line in all_genes:
    line = line.rstrip()
    if "ENSM" in line:
      all_set.add(line)
  for line in pigment_genes:
    line = line.rstrip()
    if "ENSM" in line:
      pigment_set.add(line)
  for line in stem_genes:
    line = line.rstrip()
    if "ENSM" in line:
      stem_set.add(line)
all_pigment = all_set | pigment_set
no_stem = all_pigment - stem_set
print(f'Ferret genes not associated with stem cell proliferation: {no_stem}')
pigment_and_stem = pigment_set & stem_set
print(f'Ferret genes associated with pigment and stem cell proliferation: {pigment_and_stem}')