#!/usr/bin/env python3
import sys
sequence = sys.argv[1]
sequence_upper = sequence.upper()
translation_key = sequence_upper.maketrans("ATGC","TACG")
complement = sequence_upper.translate(translation_key)
reverse_comp = complement[::-1]
print(f"{'Original Sequence':20}5'{sequence_upper} 3'\n{'Complement':20}3'{complement} 5'\n{'Reverse Complement':20}5'{reverse_comp} 3'")
