#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
from subprocess import *

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/Arya Nguyen/Experiement/ca/ca.macos", "basic.cfg"], 
            stdin=PIPE, stdout=PIPE)

for i in xrange(50):
    pid.stdin.write("3/1\n")
    x = pid.stdout.readline()
    pid.stdin.write("4/1\n")
    x = pid.stdout.readline()
    pid.stdin.write("0/1\n")
    x = pid.stdout.readline()

dataset = np.array([[0, 0]])
print 0, 0
for i in xrange(10):
    n = 0
    for j in xrange(10):
        pid.stdin.write("3/1\n")
        x = pid.stdout.readline()
        if x[0] == "1":
            n = n + 1
        pid.stdin.write("1/1\n")
        x = pid.stdout.readline()
        pid.stdin.write("4/1\n")
        x = pid.stdout.readline()
        pid.stdin.write("2/1\n")
        x = pid.stdout.readline()
        pid.stdin.write("0/1\n")
        x = pid.stdout.readline()
    dataset = np.append(dataset, [[i+1, n]], axis=0)
    print i+1, n
pid.stdin.close()

# Visualizing the output
plt.scatter(dataset[:, 0], dataset[:, 1], color='red')
plt.plot(dataset[:, 0], dataset[:, 1])
plt.title('Latent Inhibition')
plt.xlabel('Trial batch')
plt.ylabel('Responses')
plt.ylim(ymax=10)
plt.xlim(xmax=10)
plt.show()
