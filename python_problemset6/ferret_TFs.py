#!/usr/bin/env python3

tf_set = set()
stem_set = set()
with open("ferret_transcriptionFactors.tsv", "r") as trans_factors, open('ferret_stemcellproliferation_genes.tsv', 'r') as stem_genes:
  for line in trans_factors:
    line = line.rstrip()
    if "ENSM" in line:
      tf_set.add(line)
  for line in stem_genes:
    line = line.rstrip()
    if "ENSM" in line:
      stem_set.add(line)
stem_tfs = tf_set & stem_set
print(f'Ferret stem cell associated transcription factors: {stem_tfs}')