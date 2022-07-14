#!/usr/bin/env python3

import sqlite3
from tkinter.font import names
from numpy import genfromtxt
import csv

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=0)
    return data.tolist()

file_test = Load_Data('countries.csv')

file = open('countries.csv')
read_file = csv.reader(file)
header = []
header = next(read_file)

rows = []
for row in read_file:
    rows.append(row)

print(header)
print(rows)



