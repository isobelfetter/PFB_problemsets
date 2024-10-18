#!/usr/bin/env python3

import re

with open("Python_07_nobody.txt", "r") as poem, open("Python_07_nobody_sub.txt", "w") as subbed_poem:
    for line in poem:
      subbed_line = re.sub("Nobody", "Isobel", line)
      subbed_poem.write(subbed_line)

print("File written")