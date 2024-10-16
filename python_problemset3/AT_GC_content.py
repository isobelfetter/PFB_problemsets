#!/usr/bin/env python3
import sys
sequence = sys.argv[1]
print("Sequence being counted:",sequence)
sequence_upper = sequence.upper()
count_A = sequence_upper.count("A")
count_T = sequence_upper.count("T")
count_G = sequence_upper.count("G")
count_C = sequence_upper.count("C")
print(f'AT content is {count_A+count_T} bases.')
print(f'GC content is {count_G+count_C} bases.')
sequence_len = len(sequence_upper)
count_AT = count_A + count_T
count_GC = count_G + count_C
print(f'AT content is {count_AT/sequence_len :.1%}.')
print(f'GC content is {count_GC/sequence_len :.1%}.')
