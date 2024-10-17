#!/usr/bin/env python3

set1 = {3,14,15,9,26,5,35,9}
set2 = {60,22,14,0,9}
print(f'set 1: {set1}\nset 2: {set2}')
intersection = set1 & set2
print(f'intersection of set 1 and set 2: {intersection}')
set1_uniq = set1 - set2
set2_uniq = set2 - set1
print(f'unique to set 1: {set1_uniq}\nunique to set 2: {set2_uniq}')
union = set1 | set2
print(f'union of set 1 and set 2: {union}')
sym_diff = set1 ^ set2
print(f'symmetrical difference of set 1 and set 2: {sym_diff}')
