#!/usr/bin/python
from subprocess import *
import numpy as np
import matplotlib.pyplot as plt

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/Arya Nguyen/Experiement/ca/ca.macos", "basic.cfg"], 
            stdin=PIPE, stdout=PIPE)

#
# 1:UCS+, 2:UCS-, 3:CS1+, 4:CS1-, 5:CS2+, 6:CS2-
#
n = 0
while n < 40:
    pid.stdin.write("3/1\n")
    x = pid.stdout.readline()
    if x[0] == "1":
        n = n + 1
    else:
        n = 0
    pid.stdin.write("1/1\n")
    x = pid.stdout.readline()
    pid.stdin.write("4/1\n")
    x = pid.stdout.readline()
    pid.stdin.write("2/1\n")
    x = pid.stdout.readline()
    pid.stdin.write("0/1\n")
    x = pid.stdout.readline()

#pid.stdin.write("D\n")

print "Beginning 2nd order conditioning"

dataset = np.array([[0, 0]])
print 0, 0
for i in xrange(10):
    n = 0
    for j in xrange(10):
        pid.stdin.write("5/1\n")
        x = pid.stdout.readline()
        if x[0] == "1":
            n = n + 1
        pid.stdin.write("3/1\n")
        x = pid.stdout.readline()
        pid.stdin.write("6/1\n")
        x = pid.stdout.readline()
        pid.stdin.write("4/1\n")
        x = pid.stdout.readline()
        pid.stdin.write("0/1\n")
        x = pid.stdout.readline()
    dataset = np.append(dataset, [[i+1, n]], axis=0)
    print i+1, n

#pid.stdin.write("D\n")
pid.stdin.close()

# Visualizing the output
plt.plot(dataset[:, 0], dataset[:, 1], linestyle='-', marker='o')
plt.xlabel('Trial batch')
plt.ylabel('Responses')
plt.ylim(ymax=11)
plt.xlim(xmax=11)
plt.show()

