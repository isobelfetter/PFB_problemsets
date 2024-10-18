#!/usr/bin/env python3

import re
line_number = 0

with open("Python_07_nobody.txt", "r") as poem:
    for line in poem:
      line_number += 1
      for nobody in re.finditer(r"(Nobody)", line):
        if isinstance(nobody, re.Match):
          start = nobody.start(1)
          end = nobody.end(0)
          print(f"Line Number {line_number}: Nobody at {start}-{end}")
