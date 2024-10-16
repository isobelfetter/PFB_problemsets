#!/usr/bin/env python3
taxa_string = "sapiens : erectus : neanderthalensis"
print("string:", taxa_string)
taxa_list = taxa_string.split(" : ")
print(taxa_list)
print(taxa_list[1])
print(type(taxa_string))
print(type(taxa_list))
taxa_list.sort()
print(taxa_list)
