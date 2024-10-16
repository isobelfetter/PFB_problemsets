#!/usr/bin/env python3
import sys
sequence = sys.argv[1]
print("Sequence being converted:",sequence)
sequence_upper = sequence.upper()
remove_T = sequence_upper.split("T")
add_U = "U".join(remove_T)
print("Converted sequence:",add_U)
