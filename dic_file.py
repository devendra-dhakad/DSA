#!/usr/bin/env python3
import os
dir="Browser"
for name in os.listdir(dir):
    full_name=os.path.join(dir,name)
    if os.path.isdir(full_name):
        print("{} this is directory".format(full_name))
    else:
        print("{} this is file".format(full_name))
