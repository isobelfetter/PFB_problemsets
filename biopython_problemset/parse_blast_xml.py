#!/usr/bin/env python3
from Bio import Blast

blast_records = Blast.read("purH_blastp_20241020")

print(f'hits with e-value < 1e-5')

for blast_record in blast_records:
    for alignment in blast_record:
        if alignment.annotations['evalue'] < float(1e5):
            print(f'{alignment.target.id}\t{alignment.target.description}\t{alignment.annotations['evalue']}')



# for blast_record in Blast.parse(blast_file):
#     desc = blast_record.query.description
#     for alignment in blast_record:
#         e_value = alignment.annotations['evalue']
#     print(f'{desc} {e_value}')