#!/usr/bin/env python3
import sys
sequence = sys.argv[1]
print("Sequence being counted:",sequence)
sequence_upper = sequence.upper()
count_A = sequence_upper.count("A")
count_T = sequence_upper.count("T")
print(count_A, count_T)
print(f'{count_A+count_T}')
