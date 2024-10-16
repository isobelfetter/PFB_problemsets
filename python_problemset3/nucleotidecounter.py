#!/usr/bin/env python3
import sys
sequence = sys.argv[1]
print("Sequence being counted:",sequence)
sequence_upper = sequence.upper()
count_A = sequence_upper.count("A")
count_T = sequence_upper.count("T")
count_C = sequence_upper.count("C")
count_G = sequence_upper.count("G")
print(f'{count_A} A\n{count_T} T\n{count_G} G\n{count_C} C')
