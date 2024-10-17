#!/usr/bin/env python3
import sys
sequence = sys.argv[1]
sequence_upper = sequence.upper()
cut_site = sequence_upper.find("GAATTC")
print(cut_site+1)
print(f'EcoRI startPos:{cut_site+1} endPos:{cut_site+6}')
