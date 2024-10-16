#!/usr/bin/env python3
import sys
sequence = sys.argv[1]
print("Original sequence:", sequence)
sequence_upper = sequence.upper()
sub_sequence = sequence_upper[99:200]
print("100-200:",sub_sequence)
count_G = sub_sequence.count("G")
print("Number of 'G's:",count_G)
