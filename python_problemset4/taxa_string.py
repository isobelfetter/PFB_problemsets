#!/usr/bin/env python3
taxa_string = "sapiens : erectus : neanderthalensis"
print("string:", taxa_string)
taxa_list = taxa_string.split(" : ")
print(taxa_list)
print(taxa_list[1])
print(type(taxa_string))
print(type(taxa_list))
sorted_taxa = sorted(taxa_list)
print(sorted_taxa)
len_sorted_taxa = sorted(taxa_list, key = len)
print(len_sorted_taxa)
