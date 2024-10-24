#!/usr/bin/env python3

import sys

seq_length = sys.argv[1]
algo_list = ['BL50', 'BP62', 'VT160', 'VT80', 'VT40', 'VT20', 'VT10']
result_dict = {}

for matrix in algo_list:
    file_name = f'ss_{seq_length}_v_qfo_{matrix}.txt'
    with open(file_name, 'r') as read_file:
        for line in read_file:
            line = line.rstrip()
            if "#" not in line:
                values = line.split('\t')
                result_dict[matrix] = values
                break

print(f'matrix\t%iden\talen\tevalue')

for matrix in result_dict:
    values = result_dict[matrix]
    qseqid = values[0]
    sseqid = values[1]
    percid = values[2]
    alen = values[3]
    mismat = values[4]
    gaps = values[5]
    q_start = values[6]
    q_end = values[7]
    s_start = values[8]
    s_end = values[9]
    evalue = values[10]
    bits = values[11]
    print(f'{matrix}\t{percid}\t{alen}\t{evalue}')                