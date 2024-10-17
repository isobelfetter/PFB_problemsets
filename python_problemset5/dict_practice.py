#!/usr/bin/env python3
fav_dict = {'book' : 'The Martian', 'song' : 'Freebird', 'tree' : 'Eucalyptus'}
print(fav_dict['book'])
fav_thing = 'book'
print(fav_dict[fav_thing])
print(fav_dict['tree'])
fav_dict['organism'] = "sea otter"
fav_thing = 'organism'
print(fav_dict[fav_thing])

for fav in fav_dict:
  print(fav, fav_dict[fav])

import sys
fav_thing = sys.argv[1]
print(fav_dict[fav_thing])
