#!/usr/bin/python
from graph import Graph
import numpy as np
from subprocess import *

#
# 1:UCS+, 2:UCS-, 3:CS1+, 4:CS1-, 5:CS2+, 6:CS2-
#

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/Arya Nguyen/Experiement/ca/ca.macos", "basic.cfg"], stdin=PIPE, stdout=PIPE)

dataset = np.empty((0, 2), int)

for i in xrange(80):
    pid.stdin.write("3/1 5/0.9\n")
    pid.stdout.readline()
    pid.stdin.write("1/1\n")
    pid.stdout.readline()
    pid.stdin.write("4/1 6/0.9\n")
    pid.stdout.readline()
    pid.stdin.write("2/1\n")
    pid.stdout.readline()
    pid.stdin.write("0/1\n")
    pid.stdout.readline()

#pid.stdin.write("D\n")

for i in xrange(10):
    n = 0
    for j in xrange(10):
        pid.stdin.write("5/1\n")
        x = pid.stdout.readline()
        if x[0] == "1":
            n += 1
        pid.stdin.write("6/1\n")
        x = pid.stdout.readline()
        pid.stdin.write("0/1\n")
        x = pid.stdout.readline()
    dataset = np.append(dataset, [[i+1, n]], axis=0)
    print i+1, n

#pid.stdin.write("D\n")
pid.stdin.close()

# Visualizing the output
graph = Graph([(dataset[:, 0], dataset[:, 1])], 
              title='Results of a Compound Conditioning',
              file_name='plot/cmpd.png')
graph.plot_save()

