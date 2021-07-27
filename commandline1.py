#!/usr/bin/env python3
import os
import sys

file_name=sys.argv[1]

if not os.path.exists(file_name):
  with open(file_name,"w") as f:
    f.write("naw file")
else:
  print("Error,the {} already exists".format(file_name))
  sys.exit(1)
