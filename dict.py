#!/usr/bin/env python3
import csv
with open("k.txt") as file:
    red = csv.DictReader(file)
    for dict in red:
        print("{}".format())
