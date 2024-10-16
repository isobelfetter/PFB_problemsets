#!/usr/bin/env python3
import sys
sequence = sys.argv[1]
print("Sequence being converted:",sequence)
sequence_upper = sequence.upper()
remove_T = sequence_upper.split("T")
add_U = "U".join(remove_T)
print("Converted sequence:",add_U)
count_T = sequence_upper.count("T")
count_U = add_U.count("U")
print(f'{count_T} "T"s converted to {count_U} "U"s')
