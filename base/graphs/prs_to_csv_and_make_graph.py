#!/usr/bin/python
# -*- coding: utf-8 -*- 

import csv
from subprocess import call

threshold = []
precision = []
recall = []
fmeasure = []
accuracy = []
goodness = []

file = open('precision_recall_semester.txt')
with open("statistics.csv", "wb") as f:
    writer = csv.writer(f)
    i = 0
    for line in file:
        data = line.split()
        if i == 0:
            writer.writerow([data[1][:-1], data[2][1:-1], data[3][:-1], data[4][:-1], data[5][:-2], data[6][:-1], data[7][:-1], data[8][:-1], data[9][:-1], data[10]])
        else:
            writer.writerow([data[0], data[1][1:-1], data[2][:-1], data[3][:-1], data[4][:-1], data[5], data[6], data[7], data[8], data[9]])
        i += 1

call(['Rscript', 'graficas.R'])