#!/usr/bin/env python3
import csv
data=[["dev","dhakad"],["happy","londe"],["lol","hmm"]]
f=open("k.txt","w")
csv_f=csv.writer(f)
csv_f.writerows(data)
