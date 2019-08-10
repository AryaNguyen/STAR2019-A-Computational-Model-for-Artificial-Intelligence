#!/usr/bin/python
import numpy as np
import random
from subprocess import *
from graph import Graph

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/Arya Nguyen/Experiement/ca/ca.macos", "basic.cfg"], 
            stdin=PIPE, stdout=PIPE)

print "100%"

print 0, 0
dataset1 = np.array([[0, 0]])
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
    dataset1 = np.append(dataset1, [[i+1, n]], axis=0)
    print i+1, n

print
dataset2 = np.array([[0, n]])
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
    dataset2 = np.append(dataset2, [[i+1, n]], axis=0)
    print i+1, n

pid.stdin.close()

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/Arya Nguyen/Experiement/ca/ca.macos", "basic.cfg"], 
            stdin=PIPE, stdout=PIPE)

print "75%"

print 0, 0
dataset3 = np.array([[0, 0]])
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
    dataset3 = np.append(dataset3, [[i+1, n]], axis=0)
    print i+1, n

print
dataset4 = np.array([[0, 0]])
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
    dataset4 = np.append(dataset4, [[i+1, n]], axis=0)
    print i+1, n

pid.stdin.close()

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/Arya Nguyen/Experiement/ca/ca.macos", "basic.cfg"], 
            stdin=PIPE, stdout=PIPE)

print "50%"

dataset5 = np.array([[0, 0]])
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
    dataset5 = np.append(dataset5, [[i+1, n]], axis=0)
    print i+1, n

print
dataset6 = np.array([[0, n]])
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
    dataset6 = np.append(dataset6, [[i+1, n]], axis=0)
    print i+1, n

pid.stdin.close()

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/Arya Nguyen/Experiement/ca/ca.macos", "basic.cfg"], 
            stdin=PIPE, stdout=PIPE)

print "25%"

dataset7 = np.array([[0, 0]])
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
    dataset7 = np.append(dataset7, [[i+1, n]], axis=0)
    print i+1, n

print
dataset8 = np.array([[0, n]])
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
    dataset8 = np.append(dataset8, [[i+1, n]], axis=0)
    print i+1, n

pid.stdin.close()

"""
# Visualizing Conditioning with Partial reinforcement
plt.plot(dataset1[:, 0], dataset1[:, 1], linestyle='dashed', label='100%')
plt.plot(dataset3[:, 0], dataset3[:, 1], linestyle='dotted', label='75%')
plt.plot(dataset5[:, 0], dataset5[:, 1], linestyle='dashdot', label='50%')
plt.plot(dataset7[:, 0], dataset7[:, 1], linestyle='solid', label='25%')
plt.xlabel('Trial batch')
plt.ylabel('Responses')
plt.ylim(ymax=11)
plt.xlim(xmax=11)
plt.grid(True)
plt.legend()
plt.savefig('plot/partial.png')
plt.show()

# Visualizing the output
plt.plot(dataset2[:, 0], dataset2[:, 1], linestyle='dashed', label='100%')
plt.plot(dataset4[:, 0], dataset4[:, 1], linestyle='dotted', label='75%')
plt.plot(dataset6[:, 0], dataset6[:, 1], linestyle='dashdot', label='50%')
plt.plot(dataset8[:, 0], dataset8[:, 1], linestyle='solid', label='25%')
plt.xlabel('Trial batch')
plt.ylabel('Responses')
plt.ylim(ymax=11)
plt.xlim(xmax=11)
plt.grid(True)
plt.legend()
plt.savefig('plot/partial_exctinct.png')
plt.show()
"""

# Visualizing Conditioning with Partial reinforcement
graph1 = Graph([(dataset1[:, 0], dataset1[:, 1]),
               (dataset3[:, 0], dataset3[:, 1]),
               (dataset5[:, 0], dataset5[:, 1]),
               (dataset7[:, 0], dataset7[:, 1])], 
              title='Results of Partial Reinforcement',
              file_name='plot/partial.png',
              label=['100%', '75%', '50%', '25%'],
              linestyle=['dashed', 'dotted', 'dashdot', 'solid'])
graph1.plot_save()

# Visualizing the output
graph2 = Graph([(dataset2[:, 0], dataset2[:, 1]),
               (dataset4[:, 0], dataset4[:, 1]),
               (dataset6[:, 0], dataset6[:, 1]),
               (dataset8[:, 0], dataset8[:, 1])], 
              title='Results of Extinction after Partial Reinforcement',
              file_name='plot/partial_extinction.png',
              label=['100%', '75%', '50%', '25%'],
              linestyle=['dashed', 'dotted', 'dashdot', 'solid'])
graph2.plot_save()
