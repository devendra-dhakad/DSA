#!/usr/bin/env python3
import csv
data_to_save = [
  {'Author':'John Smith',    'Title':'Keep holding on',         'Pages':'326'},
  {'Author':'Erica Coleman', 'Title':'The beauty is the beast', 'Pages':'274'}
]
with open("book.txt","w") as file:
    a=csv.writer(file,fieldnames=["Author","Title","Pages"])
    a.writeheader()
    a.writerows(data_to_save)
