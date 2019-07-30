#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import random
from subprocess import *

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/Arya Nguyen/Experiement/ca/ca.macos", "basic.cfg"], 
            stdin=PIPE, stdout=PIPE)

print "100%"

dataset = np.array([[0, 0]])
print 0, 0
for i in xrange(4):
    n = 0
    for j in xrange(10):
        pid.stdin.write("3/1\n")
        x = pid.stdout.readline()
        if x[0] == "1":
            n += 1
        pid.stdin.write("1/1\n")
        pid.stdout.readline()
        pid.stdin.write("4/1\n")
        pid.stdout.readline()
        pid.stdin.write("2/1\n")
        pid.stdout.readline()
        pid.stdin.write("0/1\n")
        pid.stdout.readline()
    print i+1, n

print
dataset = np.array([[0, n]])
print 0, n
for i in xrange(10):
    n = 0
    for j in xrange(10):
        pid.stdin.write("3/1\n")
        x = pid.stdout.readline()
        if x[0] == "1":
            n += 1
        pid.stdin.write("4/1\n")
        pid.stdout.readline()
        pid.stdin.write("0/1\n")
        pid.stdout.readline()
    dataset = np.append(dataset, [[i+1, n]], axis=0)
    print i+1, n

pid.stdin.close()

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/Arya Nguyen/Experiement/ca/ca.macos", "basic.cfg"], 
            stdin=PIPE, stdout=PIPE)

print "75%"

dataset = np.array([[0, 0]])
print 0, 0
for i in xrange(4):
    n = 0
    for j in xrange(10):
        pid.stdin.write("3/1\n")
        x = pid.stdout.readline()
        if x[0] == "1":
            n += 1
        d = random.random()
        if d <= 0.75:
            pid.stdin.write("1/1\n")
            pid.stdout.readline()
        pid.stdin.write("4/1\n")
        pid.stdout.readline()
        if d <= 0.75:
            pid.stdin.write("2/1\n")
            pid.stdout.readline()
        pid.stdin.write("0/1\n")
        pid.stdout.readline()
    dataset = np.append(dataset, [[i+1, n]], axis=0)
    print i+1, n

print
dataset = np.array([[0, 0]])
print 0, n
for i in xrange(10):
    n = 0
    for j in xrange(10):
        pid.stdin.write("3/1\n")
        x = pid.stdout.readline()
        if x[0] == "1":
            n += 1
        pid.stdin.write("4/1\n")
        pid.stdout.readline()
        pid.stdin.write("0/1\n")
        pid.stdout.readline()
    dataset = np.append(dataset, [[i+1, n]], axis=0)
    print i+1, n

pid.stdin.close()

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/Arya Nguyen/Experiement/ca/ca.macos", "basic.cfg"], 
            stdin=PIPE, stdout=PIPE)

print "50%"

dataset = np.array([[0, 0]])
print 0, 0
for i in xrange(4):
    n = 0
    for j in xrange(10):
        pid.stdin.write("3/1\n")
        x = pid.stdout.readline()
        if x[0] == "1":
            n += 1
        d = random.random()
        if d <= 0.50:
            pid.stdin.write("1/1\n")
            pid.stdout.readline()
        pid.stdin.write("4/1\n")
        pid.stdout.readline()
        if d <= 0.50:
            pid.stdin.write("2/1\n")
            pid.stdout.readline()
        pid.stdin.write("0/1\n")
        pid.stdout.readline()
    dataset = np.append(dataset, [[i+1, n]], axis=0)
    print i+1, n

print
dataset = np.array([[0, 0]])
print 0, n
for i in xrange(10):
    n = 0
    for j in xrange(10):
        pid.stdin.write("3/1\n")
        x = pid.stdout.readline()
        if x[0] == "1":
            n += 1
        pid.stdin.write("4/1\n")
        pid.stdout.readline()
        pid.stdin.write("0/1\n")
        pid.stdout.readline()
    dataset = np.append(dataset, [[i+1, n]], axis=0)
    print i+1, n

pid.stdin.close()

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/Arya Nguyen/Experiement/ca/ca.macos", "basic.cfg"], 
            stdin=PIPE, stdout=PIPE)

print "25%"

dataset = np.array([[0, 0]])
print 0, 0
for i in xrange(4):
    n = 0
    for j in xrange(10):
        pid.stdin.write("3/1\n")
        x = pid.stdout.readline()
        if x[0] == "1":
            n += 1
        d = random.random()
        if d <= 0.25:
            pid.stdin.write("1/1\n")
            pid.stdout.readline()
        pid.stdin.write("4/1\n")
        pid.stdout.readline()
        if d <= 0.25:
            pid.stdin.write("2/1\n")
            pid.stdout.readline()
        pid.stdin.write("0/1\n")
        pid.stdout.readline()
    dataset = np.append(dataset, [[i+1, n]], axis=0)
    print i+1, n

print
dataset = np.array([[0, 0]])
print 0, n
for i in xrange(10):
    n = 0
    for j in xrange(10):
        pid.stdin.write("3/1\n")
        x = pid.stdout.readline()
        if x[0] == "1":
            n += 1
        pid.stdin.write("4/1\n")
        pid.stdout.readline()
        pid.stdin.write("0/1\n")
        pid.stdout.readline()
    dataset = np.append(dataset, [[i+1, n]], axis=0)
    print i+1, n

pid.stdin.close()

"""
# Visualizing the output
plt.plot(dataset[:, 0], dataset[:, 1], marker='o', markerfacecolor='red', markersize=10, linewidth=3)
plt.plot(dataset[:, 0], dataset[:, 1], linestyle='dashed')
plt.title('Latent Inhibition')
plt.xlabel('Trial batch')
plt.ylabel('Responses')
plt.ylim(ymax=10)
plt.xlim(xmax=10)
plt.show()
"""
