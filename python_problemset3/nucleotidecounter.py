#!/usr/bin/env python3
import sys
sequence = sys.argv[1]
print(sequence)
sequence_upper = sequence.upper()
count_A = sequence_upper.count("A")
count_T = sequence_upper.count("T")
count_C = sequence_upper.count("C")
count_G = sequence_upper.count("G")
print(count_A, count_T, count_G, count_C)
